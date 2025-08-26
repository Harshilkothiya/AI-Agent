from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableLambda
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()


def loader(file_name):
    loader = TextLoader(file_name, encoding='utf-8')
    doc = loader.load()
    return {'text' : doc[0]}
    # return doc


model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

prompt = PromptTemplate(
    template='Write a detailed report on the following text:\n\n{text}',
    input_variables=['text']
)

parser = StrOutputParser()

loader_runnable = RunnableLambda(loader)

chain = loader_runnable | prompt | model | parser

response = chain.invoke('d:/AI-Agent/Document_Loader/cricket.txt')
print(response)


# doc = loader('d:/AI-Agent/Document_Loader/cricket.txt')
# print(len(doc))