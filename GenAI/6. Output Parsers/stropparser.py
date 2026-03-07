from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

model = ChatOpenAI()

# Prompt with a placeholder
prompt = PromptTemplate.from_template("Tell me 3 benefits of {thing}")

# Output parser to make sure the result is a clean string
parser = StrOutputParser()

# Chain everything using |
chain = prompt | model | parser

# Call the chain
final_output = chain.invoke({"thing": "reading books"})

print("Structured Output:\n", final_output)
