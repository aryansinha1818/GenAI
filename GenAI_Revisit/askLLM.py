from openai import OpenAI
from dotenv import load_dotenv
import os

#load env variables from .env file
load_dotenv()

client = OpenAI()

response = client.responses.create(
    model = "gpt-4o-mini",
    input="explain 9 planets"
)

print(response)
print(response.output[0].content[0].text)