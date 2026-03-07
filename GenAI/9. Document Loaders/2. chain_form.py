from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

file_path = r"D:\SDE\LangChain\GenAI\9. Document Loaders\doc.txt"

loader = TextLoader(file_path,encoding='utf-8')
docs = loader.load()

prompt_template = PromptTemplate(
    template = "Give me the count of all the vowels in the following text : \n {docs}",
    input_variables=["docs"]
)

parser = StrOutputParser()

chain = (
    {"docs": RunnablePassthrough()} | prompt_template | model | parser
)

text_content = docs[0].page_content

res = chain.invoke(text_content)

print(res)