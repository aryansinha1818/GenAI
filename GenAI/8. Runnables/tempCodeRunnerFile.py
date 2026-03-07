from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a peom on {topic} in 2 lines',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'convert to hindi - {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser, prompt2, model, parser)

user_input = input("Write the topic you want poem about")
print(chain.invoke(user_input))