from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

# ✅ Tool creation
@tool
def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b this tool returns their product"""
    return a * b

llm = ChatOpenAI(model="gpt-3.5-turbo")
llm_with_tool = llm.bind_tools([multiply])

query = HumanMessage("Can you multiply 3 with 10?")
messages = [query]

result = llm_with_tool.invoke(messages)
messages.append(result)

# a type of tool msg
tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)

# We are trying to create a message history. 
print(llm_with_tool.invoke(messages).content)