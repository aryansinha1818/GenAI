from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader

loader = DirectoryLoader(
    path='name_of_your_directory',
    # whichever you want to load files from you can use glob patterns to specify file types
    glob='*.pdf *.txt', 
    loader_cls=PyPDFLoader,
    loader_cls=TextLoader,
)

docs = loader.lazy_load()

# if too many documents, then doc[0] = first document
print(docs[0].page_content)

for document in docs:
    print(document.metadata)