import langchain
from langchain_google_genai  import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperatue = 0.2)

response = model.invoke("Give the proud song on indin with 5 lines")
print(response.content)