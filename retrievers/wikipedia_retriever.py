from langchain_community.retrievers import WikipediaRetriever


retriever = WikipediaRetriever(top_k_results = 2, lang = 'en')

query = 'the geopolitical history of india and pakistan from chinese perspective'

docs = retriever.invoke(query)

print(docs)