from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
from langchain.schema.runnable import RunnableParallel
load_dotenv()


llm = HuggingFaceEndpoint(
        repo_id="google/gemma-2-2b-it",  # model being used
        task="text-generation"  # task being performed
)

model = ChatHuggingFace(llm=llm)

model2 = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Generate a short and simple notes from the following text: \n {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text: \n {text}',
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template = 'Merge the following notes and questions into a single document: \n {notes} \n {questions}',
    input_variables=["notes", "questions"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
'notes': prompt1 | model | parser,
'questions': prompt2 | model2 | parser 
})

merged_chain = prompt3 | model | parser

chain = parallel_chain | merged_chain

result = chain.invoke({"text": "Python is a high-level programming language. It is widely used for web development, data analysis, artificial intelligence, and scientific computing. Python is known for its simplicity and readability."})

chain.get_graph().print_ascii()

print(result)

