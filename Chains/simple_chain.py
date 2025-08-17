from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperatue = 0.2)

prompt = PromptTemplate(
    template="tell me 5 line about the {topic}",
    input_variables=['topic']
)

# prompt = prompt.invoke({"topic": "Python programming"})

# result = model.invoke(prompt)

# print(result.content)

chain = prompt | model
result = chain.invoke({"topic: india"})
print(result.content)

chain.get_graph().print_ascii()