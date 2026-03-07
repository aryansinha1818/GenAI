from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

video_id = "FtN3BYH2Zes"

# 1a. Indexing Document Ingestion
try:
    # If you don’t care which language, this returns the “best” one ______
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    # Flatten it to plain text
    transcript = " ".join(chunk["text"] for chunk in transcript_list)

except TranscriptsDisabled:
    print("No captions available for this video.")

# 1b. Text Splitting
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.create_documents([transcript])

# 2. Embedding generation and storing in vector store
embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
vector_store = FAISS.from_documents(chunks, embeddings)

# see a particular chunk then 
# vector_store.get_by_ids(["0"])  # replace "0" with the actual ID of the chunk you want to see

# 3. retrieval - query -- embedd
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# ✅ Final step: Ask the question and get answer from LLM
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# response = qa_chain.invoke({"query": "What is the video about?"})
# print(response["result"])

#4. augementation
# 1. Define the prompt template
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

# 2. Define the user question
question = "is the topic of aliens discussed in this video? if yes then what was discussed"

# 3. Retrieve relevant chunks (from previous steps)
retrieved_docs = retriever.invoke(question)

# 4. Merge context from retrieved documents
context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

# 5. Format the prompt with the context and question
final_prompt = prompt.format(context=context_text, question=question)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=1.2)
# qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# response = qa_chain.invoke({"query": "What is the video about?"})
# print(response["result"])

ans = llm.invoke(final_prompt)
print(ans.content)