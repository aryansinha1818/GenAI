from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header('ChatBot')

user_input = st.text_input("You: ")

llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)

if st.button('Chat'):
    result = llm.invoke(user_input)
    # it is like a print for web ui
    st.write(result.content)