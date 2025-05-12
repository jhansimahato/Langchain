from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnableSequence


load_dotenv()

#prompt template
prompt = PromptTemplate(
    input_variables=["input"],
    template="write a joke about following topic: {input}",
)
prompt2 = PromptTemplate(
    input_variables=["input"],
    template="explain the following topic in 2 lines: {input}",
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = RunnableParallel(
    {'Joke':RunnableSequence(prompt,model,parser),
     'Explanation':RunnableSequence(prompt2,model,parser) }
)

result = chain.invoke({"input":"AI"})

print(result)