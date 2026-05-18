from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 5) 

result = embedding.embed_query('Delhi is the capital of India')

print(str(result))