# build_index.py
"""
Builds vector index from preprocessed CSV data.
"""

import pandas as pd
from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings


# Reading the Dataset from the folder
try:
    df = pd.read_csv("dataset/preprocessed_data.csv")
    docs = [
        Document(
            page_content=row['summary'],
            metadata={
                "title": row['title'],
                "author": row['author'],
                "genres": row['genres'],
                "year": row['publish_year']
            }
        )
        for _, row in df.iterrows()
    ]

    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embedding_model)
    vectorstore.save_local("index/faiss_index")
    print("___________________________________________________________")
    print("Converted CSV to Vector Successfully")
    print("___________________________________________________________")
except FileNotFoundError as e:
    print(f"Error: {e}")
