import os
import json
import numpy as np
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

load_dotenv()
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_HOST = os.getenv("QDRANT_HOST")

# Load embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

dialogues_file = "michaels_dialogues.txt"

try:
    with open(dialogues_file, "r", encoding="utf-8") as file:
        dialogues = [line.strip() for line in file if line.strip()]  # Remove empty lines
except FileNotFoundError:
    print(f"Error: `{dialogues_file}` not found. Make sure the file is in the same directory.")
    exit()

print(f"Loaded {len(dialogues)} dialogues from `{dialogues_file}`")

# Generate embeddings
vectors = embedding_model.embed_documents(dialogues)
print("Generated embeddings for all dialogues.")

# Connect to Qdrant
qdrant_client = QdrantClient(url=QDRANT_HOST, api_key=QDRANT_API_KEY)

collection_name = "michael-dialogues"

# Create the collection if it doesn't exist
try:
    qdrant_client.get_collection(collection_name) 
    print(f"Collection `{collection_name}` already exists.")
except:
    print(f"Collection `{collection_name}` not found. Creating now...")
    qdrant_client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=len(vectors[0]), distance=Distance.COSINE),
    )
    print(f"Collection `{collection_name}` created successfully!")

# Upload embeddings to Qdrant
qdrant_client.upload_collection(
    collection_name=collection_name,
    vectors=vectors,
    payload=[{"text": text} for text in dialogues],
)

print("Dialogues successfully stored in Qdrant!")
