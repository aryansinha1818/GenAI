from yt_transcript import build_vector_store
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel

# 1. Build vector store
video_id = "FtN3BYH2Zes"
vector_store = build_vector_store(video_id)

# 2. Build retriever
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# 3. Prompt
prompt = PromptTemplate(
    template="""
You are a helpful assistant.
Answer ONLY from the provided transcript context.
If the context is insufficient, just say you don't know.

{context}
Question: {question}
""",
    input_variables=['context', 'question']
)

# 4. Format retrieved docs
def format_docs(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)

# 5. Build parallel input chain
parallel_chain = RunnableParallel({
    "context": retriever | RunnableLambda(format_docs),
    "question": RunnablePassthrough()
})

# 6. Combine into final chain
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=1.2)
parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

# 7. Run the chain
question = "is the topic of aliens discussed in this video? if yes then what was discussed"
answer = main_chain.invoke(question)
print(answer)
