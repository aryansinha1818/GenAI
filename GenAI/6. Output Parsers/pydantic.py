from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser
from langchain_core.prompts import PromptTemplate

# Step 1: Define schema using Pydantic
class UserInfo(BaseModel):
    name: str
    age: int
    city: str

# Step 2: Create parser from schema
parser = StructuredOutputParser.from_orm(UserInfo)

# Step 3: Add parser instructions to prompt
prompt = PromptTemplate.from_template("""
Extract the user info and return in this format:
{format_instructions}

User: Aryan is 22 years old and lives in Delhi.
""", partial_variables={"format_instructions": parser.get_format_instructions()})

# Step 4: Chain together
model = ChatOpenAI()
chain = prompt | model | parser

# Step 5: Run the chain
result = chain.invoke({})
print("Parsed Structured Output:", result)
