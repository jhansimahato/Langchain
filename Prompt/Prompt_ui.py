from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-Prover-V2-671B",  # model being used
        task="text-generation",  # task being performed
)

st.header("Research Assistant")
user_input = st.text_input("Enter your question:")

if st.button("Submit"):
    model = ChatHuggingFace(llm=llm)
    response = model.invoke(user_input)
    st.write(response.content)  # Display the response from the LLM