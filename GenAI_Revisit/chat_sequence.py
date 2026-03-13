from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

while True:
    user_input = input("You : ")

    if user_input.lower()=="exit":
        break

    response = client.responses.create(
        model="gpt-4o-mini",
        input=user_input 
    )

    print("AI : ", response.output[0].content[0].text)