from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableLambda, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

prompt = PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

generate_joke = prompt | model | parser

parallel_chain = RunnableParallel(
    {
        "joke":  RunnablePassthrough(),
        "word_count" :RunnableLambda(word_count)
    }
)

chain = generate_joke | parallel_chain

response = chain.invoke({"topic" : "AI"})
print(response)