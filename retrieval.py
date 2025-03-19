import os
from dotenv import load_dotenv
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_HOST = os.getenv("QDRANT_HOST")

# Connect to Qdrant
qdrant_client = QdrantClient(url=QDRANT_HOST, api_key=QDRANT_API_KEY)

# Load embeddings model (Hugging Face)
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load Qdrant vector store
vector_store = Qdrant(client=qdrant_client, collection_name="michael-dialogues", embeddings=embedding_model)

# Create a retriever
retriever = vector_store.as_retriever()

# Function to retrieve relevant dialogues
def retrieve_dialogues(query):
    retrieved_docs = retriever.invoke(query)
    return "\n".join([doc.page_content for doc in retrieved_docs])