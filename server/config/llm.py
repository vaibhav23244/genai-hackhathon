from dotenv import load_dotenv
from langchain_ollama import ChatOllama
# from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatOllama(model="llama3.1:8b", temperature=0.8, num_predict=1024)

# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.8)
