from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

loader = PyPDFLoader('D:\SDE\LangChain\GenAI\9. Document Loaders\Aryan_Sinha_187.pdf')

docs = loader.load()

prompt_template = PromptTemplate(
    template = "Who is Aryan Sinha? {docs}",
    input_variables=["docs"]
)

parser = StrOutputParser()

chain = (
    {"docs": RunnablePassthrough()} | prompt_template | model | parser
)

text_content = docs[0].page_content

res = chain.invoke(text_content)

print(res)