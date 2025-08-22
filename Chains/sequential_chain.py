from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)


#1 get the one best place to visit
tempate1 = PromptTemplate(
    template="give me one best palce name to visite in {contry} , give me name of the palce",
    input_variables=['contry']
)


#2 get the proper detail of that place
tempate2 = PromptTemplate(
    template="give me one day trip plane  in sort for the {place}",
    input_variables=["place"]

)

parser = StrOutputParser()


chain = tempate1 | model | parser | tempate2 | model | parser
response = chain.invoke({'contry : india'})
print(response)
chain.get_graph().print_ascii()
