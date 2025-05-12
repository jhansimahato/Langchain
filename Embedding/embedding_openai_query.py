from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-ada-002',dimensions=32)

embedding.embed_query("What is the capital of France?")