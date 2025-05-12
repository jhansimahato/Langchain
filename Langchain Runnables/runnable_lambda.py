from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough,RunnableLambda


load_dotenv()
#word counter function

def word_counter(text):
    return len(text.split())


#prompt template
prompt = PromptTemplate(
    input_variables=["input"],
    template="write a joke about following topic: {input}",
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_generator_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_counter)
})

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)

result = final_chain.invoke({"input":"AI"})

print(result)
