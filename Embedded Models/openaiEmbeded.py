from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimension=32)

documents=[
    'Delhi is the capital of India'
    'Mumbai is the capital of Maharashtra'
    'Bhubaneswar is the capital of Odidsha'
]

result=embedding.embed_documents(documents)

print(str(result))