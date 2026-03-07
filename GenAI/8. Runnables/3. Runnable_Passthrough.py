from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

passthrough = RunnablePassthrough()

prompt1 = PromptTemplate(
    template='Generate a tweet on {topic} in 2 lines',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'generate a joke on {topic} in 2 lines',
    input_variables=['topic']
)

model1 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)
model2 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

parser = StrOutputParser()

tweet_chain = RunnableSequence(prompt1, model1, parser)

parallel_chain = RunnableParallel({
    'tweet' : RunnablePassthrough(),
    'joke' : RunnableSequence(prompt2, model2, parser),
})

final_chain = RunnableSequence(tweet_chain, parallel_chain)


user_input = input("Give me a topic to generate a tweet & joke about")
result = final_chain.invoke(user_input)
print("Tweet :",  result["tweet"])
print("Joke:" , result["joke"])