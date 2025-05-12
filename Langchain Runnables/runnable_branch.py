from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough,RunnableLambda,RunnableBranch

load_dotenv()

prompt = PromptTemplate(
    input_variables=["input"],
    template="write a detailed report on {topic}",
)

conditional_prompt = PromptTemplate(
    input_variables=["text"],
    template="write a summary of the following report: {text}",
)

model = ChatOpenAI()
parser = StrOutputParser()

report_generator_chain = RunnableSequence(prompt, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(conditional_prompt, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_generator_chain, branch_chain)


result = final_chain.invoke({"topic":"AI"})
print(result)