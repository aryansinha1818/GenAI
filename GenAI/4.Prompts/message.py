from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# helpful assistance
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)

messages = [
    SystemMessage(content= "You are a helpful doctor"),
    HumanMessage(content = "Tell me about it") 
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)