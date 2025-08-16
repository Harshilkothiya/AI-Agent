from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = JsonOutputParser()

template = PromptTemplate(
    template= "write name and city of fractional character of indin \n {formate_instractions}", 
    input_variables=[],
    partial_variables={'formate_instractions': parser.get_format_instructions()}
)

# prompt = template.invoke({})
# print(prompt)

# response = model.invoke(prompt)

# print("response", response.content)

#now make this using chain

chain = template |model | parser
response = chain.invoke({})
print("response", response)