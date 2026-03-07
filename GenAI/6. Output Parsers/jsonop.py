from langchain.output_parsers import StructuredOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
from langchain_openai import ChatOpenAI

# Step 1: Define schema using Pydantic
class FictionalPerson(BaseModel):
    name: str
    age: int
    city: str

# Step 2: Create parser
parser = StructuredOutputParser.from_orm(FictionalPerson)

# Step 3: Use PromptTemplate like in your screenshot
template = PromptTemplate(
    template="Give me the name, age and city of a fictional person.\n{format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

# Step 4: Chain prompt → model → parser
model = ChatOpenAI()
chain = template | model | parser

# Step 5: Run the chain
result = chain.invoke({})

print("Parsed output as Python object:\n", result)
