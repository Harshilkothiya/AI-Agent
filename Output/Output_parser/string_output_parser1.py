from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 1 detail imformation about any topic
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)


# 2 summary of this topic
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=['text'],
)

# prompt1 = template1.invoke({'topic': 'Python programming language'})
# result = model.invoke(prompt1)
# result_parser = StrOutputParser()
# result_content = result_parser.parse(result.content)
# prompt2 = template2.invoke({'text': result_content})
# result1 = model.invoke(prompt2)
# print("content", result1.content)

# now make with chain
parser = StrOutputParser()
chain  = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic': 'oops in cpp'})
print(result)
