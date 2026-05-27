from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()
documents =[
    Document(page_content = 'langchain helps building LLM apps easily'),
    Document(page_content = "chroma is a vector database for llm based search"),
    Document(page_content = 'embeddings convert text into a high dimensional vector'),
    Document(page_content = 'langchain helps building LLM apps easily'),
]

embedding_model = OpenAIEmbeddings()

vector_store = FAISS.from_documents(
    documents = documents,
    embedding = embedding_model,
)

retriever = vector_store.as_retriever(
    search_type = 'mmr',
    search_kwargs={'k':3, 'lambda_mult':1}
)

# 0 -diverse results with less redundancy
#1 - similarity but more redundancy

results = retriever.invoke(query)