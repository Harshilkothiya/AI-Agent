from langchain.text_splitter import RecursiveCharacterTextSplitter

text = '''
hi this is harshil kothiya
this is the my ml book
this the RecursiveCharacterTextSplitter
and this is the most useable textsplitter
'''

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 25,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)