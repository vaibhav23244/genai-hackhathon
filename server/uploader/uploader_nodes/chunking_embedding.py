import re
from dotenv import load_dotenv
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_google_firestore import FirestoreVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from helpers.create_vector_index import create_firestore_vector_index
from uploader.uploader_graph_state.uploader_graph_state import GraphState

load_dotenv()

def chunking_embedding(state: GraphState):
    doc_content = state['doc_content']
    doc_name = state['doc_name']
    collection_name =  re.sub(r'[^a-zA-Z0-9_]', '_', doc_name)
    create_firestore_vector_index(f"documents_{collection_name}")
    embeddings = VertexAIEmbeddings(model_name="text-embedding-004")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(doc_content)
    vector_store = FirestoreVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection=f"documents_{collection_name}", 
    )
    return {'chunking_embdedding_status': f"Document '{doc_name}' has been chunked and embedded successfully in collection 'documents_{collection_name}'."}
