from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-small')

documents = [
    "Artificial Intelligence is transforming the way humans interact with technology by enabling machines to learn from data, recognize patterns, and make decisions with minimal human intervention, which is impacting industries such as healthcare, finance, education, and transportation at a massive scale.",

    "Machine learning models rely heavily on large datasets and computational power to train algorithms that can predict outcomes, classify information, and continuously improve their performance over time, making them highly valuable for solving complex real-world problems.",

    "The rise of cloud computing has made it easier for developers and organizations to deploy scalable applications, store vast amounts of data, and access powerful computing resources without investing heavily in physical infrastructure.",

    "Natural language processing allows computers to understand, interpret, and generate human language, enabling applications such as chatbots, virtual assistants, translation systems, and sentiment analysis tools that enhance user experience.",

    "Vector embeddings convert text into numerical representations that capture semantic meaning, allowing systems to perform similarity search, recommendation, and retrieval tasks efficiently, which is a key concept in building modern AI applications like RAG systems."
]

query = "tell me about ml"
# 2 line should be the ans

# we find the docu embed

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

doc_scores = cosine_similarity([query_embedding], doc_embeddings)[0]
doc_indices = np.argsort(doc_scores)[::-1]

print(documents[doc_indices[0]])