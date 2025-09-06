from dotenv import load_dotenv
# from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.8)
# llm = ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct", temperature=0.8)