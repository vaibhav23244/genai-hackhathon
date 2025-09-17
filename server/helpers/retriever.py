import re
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_google_firestore import FirestoreVectorStore

def get_retriever(doc_name: str):
    collection_name = re.sub(r'[^a-zA-Z0-9_]', '_', doc_name)
    embeddings = VertexAIEmbeddings(model_name="text-embedding-004")
    vector_store = FirestoreVectorStore(
        collection=f"documents_{collection_name}",
        embedding_service=embeddings  
    )
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    return retriever
