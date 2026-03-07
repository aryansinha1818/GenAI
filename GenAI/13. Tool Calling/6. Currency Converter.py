from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import InjectedToolArg
from typing import Annotated
import requests
import json 
import dotenv
dotenv.load_dotenv()

# 1. tool create 
@tool
def get_conversion(base_currency: str, target_currency: str) -> float:
    """
    Get the conversion rate between two currencies.
    Args:
        base_currency: The base currency to convert from.
        target_currency: The target currency to convert to.
    Returns:
        The conversion rate between the two currencies.
    """
    url = f"https://v6.exchangerate-api.com/v6/ba60ca1d93bb091b22649f82/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    return data["conversion_rate"]

@tool
def convert(base_currency_value:int, conversion_rate: Annotated[float, InjectedToolArg ]) -> float:
    # ❌ "LLM, do not try to fill this argument."
    # ✅ "(I the developer/runtime) will inject this value after running earlier tools."
    """
    Convert a value from one currency to another.
    Args:
        base_currency_value: The value to convert.
        conversion_rate: The conversion rate between the two currencies.
    Returns:
        The converted value.
    """
    return base_currency_value * conversion_rate

# manual single tool call for testing
# rate = get_conversion.invoke({"base_currency": "EUR", "target_currency": "INR"})
# value = convert.invoke({"base_currency_value": 100, "conversion_rate": rate})

# binding
llm = ChatOpenAI(model="gpt-3.5-turbo")
llm_with_tool = llm.bind_tools([get_conversion, convert])

print("Welcome to currency converter bot!")
base = input("Enter the base currency: ")
target = input("Enter the target currency: ")
amount = input("Enter the amount: ")
# user query
messages = [HumanMessage(content=f"What is the conversion factor between {base} and {target}? and based on that can you convert {amount} {base} to {target}?")]


# LLM processes the input and decides which tools to call
ai_message = llm_with_tool.invoke(messages)
messages.append(ai_message)

# Loop through the tools the model wants to call
for tool_call in ai_message.tool_calls:
    if tool_call["name"] == "get_conversion":
        # Run get_conversion tool
        tool_result = get_conversion.invoke(tool_call["args"])
        conversion_rate = tool_result  # store the float
        messages.append(ToolMessage(tool_call_id=tool_call["id"], content=str(tool_result)))  # add result as string

    if tool_call["name"] == "convert":
        # Inject conversion_rate into the args manually
        tool_call["args"]["conversion_rate"] = conversion_rate
        tool_result = convert.invoke(tool_call["args"])
        messages.append(ToolMessage(tool_call_id=tool_call["id"], content=str(tool_result)))  # add result as string

# Now pass the full updated conversation again to get the final answer
final_response = llm_with_tool.invoke(messages)

print(final_response.content)
