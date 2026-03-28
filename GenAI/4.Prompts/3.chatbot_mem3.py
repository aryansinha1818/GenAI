from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []



while True:
    user_input = input("You : ")
    if user_input == "exit":
        break
    result = model.invoke(user_input, chat_history)
    chat_history.append((user_input, result.content))
    print("AI : ", result.content)

print(chat_history)
# all messages are stored all at once but we don't know who send to whom