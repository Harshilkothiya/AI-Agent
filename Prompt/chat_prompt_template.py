from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# List of Messages

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domin} expert. give the ans in sort turm no need to explain"),
    ("human", "tell me about {topic}")
])

prompt =  chat_template.invoke({"domin":"cricket", "topic":"IPL 2023"})

response = model.invoke(prompt)
chat_template.append(("ai", response.content))

print(response.content)
print(chat_template)