from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Step 1: Define response schema (like your screenshot)
schemas = [
    ResponseSchema(name="fact_1", description="First fun fact about space"),
    ResponseSchema(name="fact_2", description="Second fun fact about space"),
]

# Step 2: Create parser from response schemas
parser = StructuredOutputParser.from_response_schemas(schemas)

# Step 3: Prompt with parser's format instruction
prompt = PromptTemplate(
    template="Give me two fun facts about space.\n{format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Step 4: Set up model and chain
model = ChatOpenAI()
chain = prompt | model | parser

# Step 5: Run the chain
result = chain.invoke({})
print("Structured Output:\n", result)
