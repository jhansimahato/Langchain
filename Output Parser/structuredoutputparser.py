from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()


llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.2-3B-Instruct",  # model being used
        task="text-generation"  # task being performed
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1',description='a fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='a fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='a fact 3 about the topic'),
    ResponseSchema(name='fact_4',description='a fact 4 about the topic'),
    ResponseSchema(name='fact_5',description='a fact 5 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give me 5 facts about the topic {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()}
)

prompt = template.invoke({'topic': 'cats'})
result = model.invoke(prompt)
final_parser = parser.parse(result.content)

print(final_parser)