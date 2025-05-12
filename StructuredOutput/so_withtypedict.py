from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal

load_dotenv()


llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.2-3B-Instruct",  # model being used
        task="text-generation"  # task being performed
)

model = ChatHuggingFace(llm=llm)


class Review(TypedDict):
    summary: str
    sentiment: str


class Review_Annoted(TypedDict):
    key_themes: Annotated[list[str],"A list of key themes or topics in the review"]
    summary: Annotated[str,"A breif summary of the review"]
    sentiment: Annotated[Literal["POS","NEG"],"The sentiment of the review, either positive or negative"]
    pros: Annotated[Optional[list[str]],"A list of pros or positive aspects of the product"]
    cons: Annotated[Optional[list[str]],"A list of cons or negative aspects of the product"]
stuructured_model = model.with_structured_output(Review_Annoted)

result = stuructured_model.invoke(" The hardware is great, but the software is not.There are many pre-installed app that I cannot remove. Also, The UI looks outdated compared to other brands.")

print(result)

