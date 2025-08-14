import streamlit as st
from langchain_google_genai  import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

st.title("This is the Simple Chat Model")

user_input = st.text_input("Enter your query here")

if st.button("Submmit"):

    model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperatue = 0.2)

    response = model.invoke(user_input)
    st.write(response.content)