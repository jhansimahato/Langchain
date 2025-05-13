from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader


loader = DirectoryLoader(
    path ="Document Loader\Books",
    glob="*.pdf",
    loader_cls=PyPDFLoader,
)

# loader 
docs = loader.load()

# lazy loading 

document = loader.lazy_load() 

print(type(docs))
print(len(docs))
