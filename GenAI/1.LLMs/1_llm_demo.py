# //openai ke apckage se baat kaise karni hai
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# takes string and returns string 
llm = OpenAI(model= 'gpt-3.5-turbo-instruct')

res = llm.invoke("What is the capital of India?")
print(res)