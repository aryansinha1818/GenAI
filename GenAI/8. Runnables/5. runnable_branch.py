from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a 2 line report on {topic}',
    input_variable=['topic']
)

prompt2 = PromptTemplate(
    template = 'summerize the following text \n {text}',
    input_variable=['topic']
)

model = ChatOpenAI(model="gpt-3.5-turbo")

parser = StrOutputParser()

# report_chain = RunnableSequence(prompt1, model, parser)
report_chain = prompt1|model| parser

branch_chain = RunnableBranch(
    # (condition ,runnable),
    (lambda x: len(x.split())>10, RunnableSequence(prompt2, model, parser))
    , RunnablePassthrough()
)

final_chain = RunnableSequence(report_chain, branch_chain)

print(final_chain.invoke({'topic':'Tech world in 2026'}))