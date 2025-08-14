from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# List of Messages

message = [
    SystemMessage(content="You are a helpful assistant. give the ans in sort turm no need to explain"),
    HumanMessage(content="tell me about Langchain")
]

response = model.invoke(message)
message.append(AIMessage(content=response.content))

print(response.content)w
print(message)