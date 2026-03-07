from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model = "gpt-3.5-turbo", temperature = 0.8, max_completion_tokens=10)

res = llm.invoke("Give me a poem on Rain")

print(res.content)