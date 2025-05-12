from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not token:
    print("❌ HuggingFace API token not found.")
else:
    print("✅ HuggingFace API token is loaded.")


load_dotenv()


llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-Prover-V2-671B",  # model being used
        task="text-generation",  # task being performed
)

model = ChatHuggingFace(llm=llm)
print("✅ Model loaded successfully.")

result = model.invoke("what is the capital of India")
print(result.content)
