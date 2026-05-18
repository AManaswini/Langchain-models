from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

text = 'Delhi is the capital of Inida'

# vector = embedding.embed_query(text)

# print(str(vector))

documents = [
   'Delhi is the capital of India',
   'Sacramento is the capital of california',
   'Hyderabad is the capital of Telangana'
]

vector2= embedding.embed_documents(documents)

print(vector2)