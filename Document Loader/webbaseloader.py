
from langchain_community.document_loaders import WebBaseLoader

url = 'https://github.com/campusx-official/langchain-document-loaders/blob/main/webbase_loader.py'


loader = WebBaseLoader(url)

docs = loader.load()

print(type(docs))
print(len(docs))
print(docs[0].metadata) 
print(docs[0].page_content)

