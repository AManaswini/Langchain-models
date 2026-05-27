vector_store = Chroma(
    embedding_function = OpenAIEmbeddings(),
    persist_directory = 'my_chroma_db',
    collection_name = 'sample'
)

vector_store.add_documents(docs)

vector_store.get(include = ['embeddings', 'metadata'])

vector_store.similarity_search(
    query = 'who is the bowler aong these?',
    k=2 
)

vector_store.similarity_search_with_score(
    query="",
    filter = {'team':'Chennai Super Kings'}
)

vector_store.update_document(
    document_id = '',
    document= 'updated document'
)

vector_store.delete(ids = ['id1'])