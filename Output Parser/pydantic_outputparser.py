from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()


llm = HuggingFaceEndpoint(
        repo_id="google/gemma-2-2b-it",  # model being used
        task="text-generation"  # task being performed
)

model = ChatHuggingFace(llm=llm)


class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(gt=18, description="The age of the person")
    city: str = Field(description="The city of the person")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Give me the name, age and city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={
        "format_instruction": parser.get_format_instructions()}

)

prompt = template.invoke({'place': 'New York'})
model_response = model.invoke(prompt)
final_result = parser.parse(model_response.content)
print(final_result)

