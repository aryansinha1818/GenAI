from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough


load_dotenv()

url = "https://www.flipkart.com/search?q=healthy%20food&otracker=search"
loader = WebBaseLoader(url)
docs = loader.load()


prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Webpage content:
{context}

User question:
{question}

Answer the question based only on the above webpage content.
"""
)


model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()


chain = (
    {"context": lambda _: docs[0].page_content, "question": RunnablePassthrough()}
    | prompt_template
    | model
    | parser
)

question = input("Ask your question based on the Flipkart webpage: ")

res = chain.invoke(question)


print("\nAnswer:\n", res)
