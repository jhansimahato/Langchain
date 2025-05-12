from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.2-3B-Instruct",  # model being used
        task="text-generation"  # task being performed
)

model = ChatHuggingFace(llm=llm)


# Pipeline: Topic - LLM - detailed_report - LLM - Summary

template1= PromptTemplate(
    template = "write a detailed report on the following topic: {topic}",
    input_variables = ["topic"]
)

template2 = PromptTemplate(
    template = "write a 5 line summary of the following report: {report}",
    input_variables = ["report"]
)

# without stroutputparser

# prompt1 = template1.invoke({'topic':'Blackhole'})

# result = model.invoke(prompt1)

# prompt2 = template2.invoke({'report':result.content})

# final_result = model.invoke(prompt2)


parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

final_result = chain.invoke({'topic':'Blackhole'})

print(final_result)



