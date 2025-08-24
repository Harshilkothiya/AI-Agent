from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableLambda
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from dotenv import load_dotenv

load_dotenv()


loader = DirectoryLoader(
    path='d:/Research paper',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# doc = loader.load()

# print(len(doc))

# print(doc[22].page_content)



#lazy loading 

doc = loader.lazy_load()

for d in doc:
    print(d.metadata)
    print(d.page_content)
