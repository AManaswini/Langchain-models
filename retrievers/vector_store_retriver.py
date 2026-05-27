from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()
documents =[
    Document(page_content = 'langchain helps building LLM apps easily'),
    Document(page_content = "chroma is a vector database for llm based search"),
    Document(page_content = 'embeddings convert text into a high dimensional vector')
]

embedding_model = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(
    documents =documents,
    embedding = embedding_model,
    collection_name = 'my_collection'
)

retriever = vectorstore.as_retriever(search_kwargs = {'k':2})

query = 'what is chroma db?'

results = retriever.invoke(query)

print(results)
