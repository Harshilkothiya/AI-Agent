from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader


loader = TextLoader("./text.txt")
doc = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(doc)
# splitter.split_text(text) in this function we need pass text as string fromat

print(len(result))
print(result[0])