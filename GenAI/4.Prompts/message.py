from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# helpful assistance
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini', temperature=1)

#human messgae - we send it to the ai, say, what is the capital of India?
# system message : what the chat bot is? what is the context?
messages = [
    SystemMessage(content= "You are a helpful doctor"),
    HumanMessage(content = "Tell me about maleria by ant bite") 
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)