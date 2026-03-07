import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool, InjectedToolArg
from typing import Annotated
import requests
import dotenv

dotenv.load_dotenv()

# --- TOOLS ---

@tool
def get_conversion(base_currency: str, target_currency: str) -> float:
    """Get the conversion rate between two currencies."""
    url = f"https://v6.exchangerate-api.com/v6/ba60ca1d93bb091b22649f82/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    
    # Error handling
    if data.get("result") != "success":
        raise ValueError("Invalid currency code or API error.")
    
    return data["conversion_rate"]

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """Convert a value from one currency to another."""
    return base_currency_value * conversion_rate

# --- LLM SETUP ---
llm = ChatOpenAI(model="gpt-3.5-turbo")
llm_with_tool = llm.bind_tools([get_conversion, convert])

# --- STREAMLIT UI ---
st.title("💱 Currency Converter Bot")

base = st.text_input("Enter base currency (e.g., EUR)", "EUR").upper()
target = st.text_input("Enter target currency (e.g., INR)", "INR").upper()
amount = st.number_input("Enter amount", min_value=1, value=100)

if st.button("Convert"):
    with st.spinner("Converting..."):
        try:
            # 1. Build user query
            prompt = (
                f"What is the conversion factor between {base} and {target}? "
                f"And based on that can you convert {amount} {base} to {target}?"
            )
            messages = [HumanMessage(content=prompt)]

            # 2. LLM decides tool calls
            ai_message = llm_with_tool.invoke(messages)
            messages.append(ai_message)

            for tool_call in ai_message.tool_calls:
                if tool_call["name"] == "get_conversion":
                    tool_result = get_conversion.invoke(tool_call["args"])
                    conversion_rate = tool_result
                    messages.append(ToolMessage(tool_call_id=tool_call["id"], content=str(tool_result)))

                if tool_call["name"] == "convert":
                    tool_call["args"]["conversion_rate"] = conversion_rate
                    tool_result = convert.invoke(tool_call["args"])
                    messages.append(ToolMessage(tool_call_id=tool_call["id"], content=str(tool_result)))

            # 3. Final LLM message
            final_response = llm_with_tool.invoke(messages)

            st.info(f"💱 1 {base} = {conversion_rate:.2f} {target}")
            st.success(f"✅ {amount} {base} = {tool_result:.2f} {target}")

        except Exception as e:
            st.error(f"Error: {e}")
