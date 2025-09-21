import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()

SERVICE_ACCOUNT_FILE = os.path.join(os.getcwd(), "gcp-key.json")
PROJECT_ID = os.getenv("PROJECT_ID") 

def create_firestore_vector_index(collection_id: str, dimension: int = 768):
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
    service = build("firestore", "v1", credentials=credentials)

    parent = f"projects/{PROJECT_ID}/databases/(default)/collectionGroups/{collection_id}"

    body = {
        "fields": [
            {
                "fieldPath": "embedding",
                "vectorConfig": {
                    "dimension": dimension,
                    "flat": {}
                }
            }
        ],
        "queryScope": "COLLECTION"
    }

    request = service.projects().databases().collectionGroups().indexes().create(
        parent=parent,
        body=body
    )

    response = request.execute()
    print(f"✅ Vector index creation initiated for collection '{collection_id}':", response)
    return response
