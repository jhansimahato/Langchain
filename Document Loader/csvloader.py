from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("Document Loader\Social_Network_Ads.csv")

data = loader.load()

print(data[0])
print(len(data))
print(type(data))