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

result = llm_with_tool.invoke("What is the product of 3 and 4?")

# This would give the result in the format {"a":1,"b":3}
print(result.tool_calls[0]['args'])

# We send the args and then the multiply tool returns the result
# ans = multiply.invoke(result.tool_calls[0]['args'])
# print(ans)

# ans = multiply.invoke(result.tool_calls[0])
# print(ans)

# Have a package wrapped around under tool_message to do so get the output from here and then paste in the next code
# print(result.tool_calls[0])

# tool_message
ans = multiply.invoke({'name': 'multiply', 'args': {'a': 3, 'b': 4}, 'id': 'call_a5QBWsd9Hi4Hwqqw1rc3UKwC', 'type': 'tool_call'})
print(ans)

