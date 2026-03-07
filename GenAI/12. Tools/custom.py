from langchain_core.tools import tool

# 1. create a function
# add type hints to the function
# add decorator to the function
def multiply(a,b):
    """DocString : Multiplies two numbers."""
    return a * b
def multiply(a: int, b: int) -> int:
    """DocString : Multiplies two numbers."""
    return a * b

# 2. add a tool decorator to the function
@tool
def multiply(a: int, b: int) -> int:
    """DocString : Multiplies two numbers."""
    return a * b

result = multiply.invoke({"a": 2, "b":  3})
print("Result of multiplication:", result)
print(multiply.name)
print(multiply.description)
print(multiply.metadata)
