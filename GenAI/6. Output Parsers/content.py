from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI()

# First prompt
template1 = PromptTemplate.from_template("Tell me a fun fact about {topic}")
prompt = template1.invoke({"topic": "space"})

# Get the response
res = model.invoke(prompt)
print("First model response:", res.content)

# Second prompt that uses result from first
template2 = PromptTemplate.from_template("Can you make a short poem using this text: {text}")
prompt2 = template2.invoke({'text': res.content})

# Second model call
result1 = model.invoke(prompt2)
print("Final poem:", result1.content)
