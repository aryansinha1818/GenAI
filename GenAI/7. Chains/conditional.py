from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

# Models
model1 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
model2 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Prompt
prompt = PromptTemplate.from_template("Write a short note about {topic}")

# Output parser
parser = StrOutputParser()

# Full chains
smart_chain = prompt | model1 | parser
fast_chain = prompt | model2 | parser

# Conditional logic using RunnableBranch
conditional_chain = RunnableBranch(
    (lambda x: x["mode"] == "smart", smart_chain),
    (lambda x: x["mode"] == "fast", fast_chain),
    # default fallback
    smart_chain
)

input1 = {"topic": "Jupiter", "mode": "smart"}  
input2 = {"topic": "Saturn", "mode": "fast"}    

print("Smart Output:\n", conditional_chain.invoke(input1))
print("Fast Output:\n", conditional_chain.invoke(input2))
