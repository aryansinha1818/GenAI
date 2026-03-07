from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

# ✅ Tool creation
@tool
def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b this tool returns their product"""
    return a * b

# ✅ Tool usage (direct invocation, not tool calling)
# print(multiply.invoke({'a': 3, 'b': 4}))

# print(multiply.description)
# print(multiply.metadata)
# print(multiply.args)

llm = ChatOpenAI(model="gpt-3.5-turbo")
llm_with_tool = llm.bind_tools([multiply])

# We get an ai message, no need to use any tool
print(llm_with_tool.invoke("Hi"))

# Now the llm knows that we want to use the multiply tool
print(llm_with_tool.invoke("Can you multiply 3 with 10?"))

# Now calling an attribute, gives a list of dictionary
print(llm_with_tool.invoke("Can you multiply 3 with 10?").tool_calls)