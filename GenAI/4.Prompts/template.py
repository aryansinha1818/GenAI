from langchain_core.prompts import ChatPromptTemplate


chat_template = ChatPromptTemplate([
    ('system', 'You are a {mode}' ),
    ('human', ' Explain in simple terms what {purpose} of 2*4+2?')
    
])

prompt = chat_template.invoke({'mode' : 'teacher',
                              'purpose' : 'bodmas calc'})

print(prompt)