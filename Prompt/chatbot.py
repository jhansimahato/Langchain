from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()


llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-Prover-V2-671B",  # model being used
        task="text-generation" # task being performed
)

chat_history = []  # Initialize chat history

while True:
    user_input = input("You: ")
    chat_history.append(user_input) # Initialize chat hist
    if user_input == "exit":
        break

    model = ChatHuggingFace(llm=llm)
    result = model.invoke(user_input)
    chat_history.append(result.content)  # Append the model's response to chat histor
    print("Assistant:", result.content)  # Display the response from the LLM