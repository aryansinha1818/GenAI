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

# You’re not getting the final answer (like "12") because GPT is stopping after deciding to call the tool — it doesn't execute the tool itself. Instead, it returns a tool_calls request, saying: “Please run this tool and then give me the result.” Since you’re using llm.bind_tools(...) directly, it only returns the tool call instruction, not the actual answer. To get the full response, you either need to manually run the tool and pass the result back to GPT, or use a LangChain agent, which handles the tool execution and response flow automatically.
response = llm_with_tool.invoke("What is the product of 3 and 4?")
print(response)