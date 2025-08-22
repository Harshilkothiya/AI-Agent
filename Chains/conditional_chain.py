from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

class Feedback(BaseModel):
    sentiment : Literal["positive", "negative"] = Field(description="give me the sentiment of the feedback")

parser = StrOutputParser()
parser1 = PydanticOutputParser(pydantic_object=Feedback)

prompt = PromptTemplate(
    template="Classify the sentiment of the following feedback text into postive or negative \n {text} \n {format_instruction}",
    input_variables=['text'],
    partial_variables={'format_instruction': parser1.get_format_instructions()}
)

prompt1 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt2 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

classifier_chain = prompt | model | parser1

branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive', prompt1 | model | parser),
    (lambda x : x.sentiment == "negative", prompt2 | model | parser),
    RunnableLambda(lambda x : "can not find the sentiment")
)

chain = classifier_chain | branch_chain

response = chain.invoke({"text":"this is the worst phone"})

print(response)