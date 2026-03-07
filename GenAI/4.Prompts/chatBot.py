from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)

chat_history = [
SystemMessage(content= 'You are a helpful doctor')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    res = model.invoke(chat_history)
    chat_history.append(AIMessage(res.content))
    print("AI: ", res.content)

print(chat_history)