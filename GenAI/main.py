from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence
from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

prompt = PromptTemplate.from_template(
    "You are a calculator.\n"
    "Take the two numbers and perform the given operation.\n\n"
    "num1: {num1}\n"
    "num2: {num2}\n"
    "operation: {operation}\n\n"
    "Return the result in this JSON format:\n"
    "{{\n"
    "  \"operation\": \"{operation}\",\n"
    "  \"num1\": {num1},\n"
    "  \"num2\": {num2},\n"
    "  \"result\": <your computed result>\n"
    "}}"
)


model = ChatOpenAI(model="gpt-3.5-turbo")

parser = JsonOutputParser()

# 4. Create the chain: Prompt → Model → JSON Parser
chain = prompt | model | parser

# 5. Run the chain
result = chain.invoke({
    "num1": 2,
    "num2": 3,
    "operation": "add"
})

# 6. Print the parsed Python dict
print(result)



