from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# Schema - to only return either +ve or -ve
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="Give the sentiment of the feedback"
    )
# Forces LLM to output structured data
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Classification prompt
prompt1 = PromptTemplate(
    template="""
Classify the sentiment of the following feedback text into positive or negative.

{feedback}

{format_instruction}
""",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()}
)

# IMPORTANT FIX → keep feedback + sentiment
classifier_chain = (
    prompt1
    | model
    | parser2
    | RunnableLambda(lambda x: {"sentiment": x.sentiment})
)

# Response prompts
prompt2 = PromptTemplate.from_template(
    "Write an appropriate response to this positive feedback:\n{feedback}"
)

prompt3 = PromptTemplate.from_template(
    "Write an appropriate response to this negative feedback:\n{feedback}"
)

# Merge feedback + sentiment
merge_input = RunnableLambda(
    lambda x: {"feedback": x["feedback"], "sentiment": x["sentiment"]}
)

#  bool check(x){
# return x["sentiment"] == "positive";}
# Branch logic
branch_chain = RunnableBranch(
    (lambda x: x["sentiment"] == "positive", prompt2 | model | parser),
    (lambda x: x["sentiment"] == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not determine sentiment")
)

# Final chain
chain = (
    {"feedback": lambda x: x["feedback"]}
    | RunnableLambda(lambda x: {
        "feedback": x["feedback"],
        **classifier_chain.invoke({"feedback": x["feedback"]})
    })
    | branch_chain
)

print(chain.invoke({"feedback": "This is a terrible phone"}))