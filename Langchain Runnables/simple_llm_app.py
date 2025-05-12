from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


#Initialise the LLM 
llm = OpenAI(temperature=0.9)

# Create a prompt template

prompt = PromptTemplate(
    input_variables=["input"],
    template = "Suggesr a catchy blog title about {topic}"
)

#Define the input 
topic = input("Enter a topic: ")

formatted_prompt = prompt.format(input=topic)

blog_title = llm(formatted_prompt)

print(f"Suggested blog title: {blog_title}")