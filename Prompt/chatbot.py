from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  
from dotenv import load_dotenv

load_dotenv()

chat = [
    SystemMessage(content="You are a helpful assistant. Provide concise answers without unnecessary explanations."),
]

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

while True:
    user_input = input("You: ")


    if user_input.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break
    
    chat.append(HumanMessage(content=user_input))
    response = model.invoke(chat)

    print(f"AI: {response.content}")
    chat.append(AIMessage(content=response.content))

print(chat)

