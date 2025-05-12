from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


llm = HuggingFaceEndpoint(
        repo_id="google/gemma-2-2b-it",  # model being used
        task="text-generation"  # task being performed
)

model = ChatHuggingFace(llm=llm)

template = PromptTemplate(
    template="Give 5 interesting facts about {topic}",
    input_variables=["topic"]
)

parser =  StrOutputParser()

chain = template | model | parser
chain.invoke({"topic": "Python programming"})

chain.get_graph().print_ascii()