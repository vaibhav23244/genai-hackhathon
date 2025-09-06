import os
from dotenv import load_dotenv
from graph_state import GraphState
from langchain_google_community import GCSFileLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.getcwd(), "gcp-key.json")

def doc_content_extractor(state: GraphState):
    doc_name = state['doc_name']
    loader = GCSFileLoader(project_name=os.getenv("PROJECT_NAME"), bucket=os.getenv("BUCKET_NAME"), blob=doc_name)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(documents)
    doc_content = [doc.page_content for doc in split_docs]
    return {"doc_content_chunks": doc_content}