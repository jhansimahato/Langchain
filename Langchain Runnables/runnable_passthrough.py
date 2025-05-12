from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough


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

# This will only return the explanation and not the joke in order to get both we use Runnablepassthrough
# chain = RunnableSequence(prompt,model,parser,prompt2,model,parser)

# result = chain.invoke({"input":"AI"})

# print(result)

passthrough = RunnablePassthrough()

joke_generator_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'explanation': RunnableSequence(prompt2, model, parser)
    }
)

final_chain = RunnableSequence(joke_generator_chain,parallel_chain)

result = final_chain.invoke({"input":"AI"})

print(result)