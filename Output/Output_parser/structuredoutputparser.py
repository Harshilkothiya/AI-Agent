from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

schama = [
    ResponseSchema(name="name", description="Name of the character"),
    ResponseSchema(name="city", description="City of the character")
]

parser = StructuredOutputParser.from_response_schemas(schama)

template = PromptTemplate(
    template= "write name and city of fractional character of indin \n {formate_instractions}", 
    input_variables=[],
    partial_variables={'formate_instractions': parser.get_format_instructions()}
)

chain = template | model | parser
response = chain.invoke({}) 

print(response)