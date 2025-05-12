from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence


load_dotenv()

#prompt template
prompt = PromptTemplate(
    input_variables=["input"],
    template="write a joke about following topic: {input}",
)
prompt2 = PromptTemplate(
    input_variables=["input"],
    template="explain the following joke: {input}",
)

model = ChatOpenAI()

parser = StrOutputParser()


chain = RunnableSequence(prompt,model,parser,prompt2,model,parser)

result = chain.invoke({"input":"AI"})

print(result)