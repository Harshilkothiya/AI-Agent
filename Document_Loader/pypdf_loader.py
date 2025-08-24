from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableLambda
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

load_dotenv()


loader = PyPDFLoader('d:/AI-Agent/Document_Loader/research_paper_new.pdf')

doc = loader.load()

print(doc[0].metadata)
print(doc[0].page_content)

# this is use only when we have pdf which have only text init.