from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableLambda
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = "https://data-lync.vercel.app/"

loader = WebBaseLoader(url)
doc = loader.load()

chain =  prompt | model | parser

response = chain.invoke({"question":"what is the name of the company", "text":doc[0].page_content}) 
print(response)