from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", dimention=10)

dist = [
    "Ms Dhoni is a great cricketer",
    "Sachin Tendulkar is a legendary batsman",
    "Virat Kohli is a modern cricket icon",
    "Rohit Sharma is known for his explosive batting",
    "Jasprit Bumrah is a world-class bowler"
]

qury = "Who is the best cricketer in India?"

doc_embeddings = model.embed_documents(dist)
query_embedding = model.embed_query(qury)

score = cosine_similarity([query_embedding], doc_embeddings)[0]

index = np.argmax(score)
print(dist[index])
