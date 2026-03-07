# chain_base.py

from yt_transcript2 import get_transcript_chunks

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel

# 1. Setup
video_id = "FtN3BYH2Zes"

# 2. Get transcript chunks from yt_transcript.py
chunks = get_transcript_chunks(video_id)

# 3. Create a fresh vector store (not shared from yt_transcript)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = FAISS.from_documents(chunks, embeddings)

# 4. Build retriever
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# 5. Prompt template
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

# 6. Function to format docs
def format_docs(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)

# 7. Parallel input pipe
parallel_chain = RunnableParallel({
    "context": retriever | RunnableLambda(format_docs),
    "question": RunnablePassthrough()
})

# 8. Final chain: prompt → LLM → parser
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=1.2)
parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

# 9. Run the query
question = "is the topic of aliens discussed in this video? if yes then what was discussed"
answer = main_chain.invoke(question)

print("\n🤖 Answer:\n", answer)
