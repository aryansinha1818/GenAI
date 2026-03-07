from langchain_community.document_loaders import TextLoader

file_path = r"D:\SDE\LangChain\GenAI\8. Document Loaders\doc.txt"
loader = TextLoader(file_path, encoding='utf-8')

docs = loader.load()

print(len(docs))

print(docs[0])

print(type(docs))

# page_content
# metadata


