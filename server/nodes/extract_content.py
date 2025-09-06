import os
from dotenv import load_dotenv
from graph_state import GraphState
from langchain_google_community import GCSFileLoader

load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.getcwd(), "gcp-key.json")

def extract_content(state: GraphState):
    doc_name = state["doc_name"]
    loader = GCSFileLoader(
        project_name=os.getenv("PROJECT_NAME"),
        bucket=os.getenv("BUCKET_NAME"),
        blob=doc_name
    )
    documents = loader.load()
    return {
        "doc_content": "".join(doc.page_content for doc in documents)
    }
