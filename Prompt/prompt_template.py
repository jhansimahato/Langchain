from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()


llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1",  # model being used
        task="text-generation"  # task being performed
)

template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

st.header("Research Assistant")
user_input = st.text_input("Enter your Name:")

if st.button("Submit"):
    model = ChatHuggingFace(llm=llm)
    prompt = template2.invoke({'name':user_input})  # Format the prompt with user input
    response = model.invoke(prompt)
    st.write(response.content)  # Display the response from the LLM