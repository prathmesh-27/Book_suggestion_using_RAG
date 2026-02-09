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
    # df = df.head(50) #For checking if this is working or not
    docs = [
        Document(
            page_content=f"""
            Title: {row['title']}
            Author: {row['author']}
            Publish Year: {row['publish_year']}
            Genres: {row['genres']}
            Summary: {row['summary']}
            """.strip(),
            metadata={
                "title": row['title'],
                "author": row['author'],
                "genres": row['genres'],
                "year": row['publish_year']
            }
        )
        for _, row in df.iterrows()
    ]

    # embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )
    vectorstore = FAISS.from_documents(docs, embedding_model)
    vectorstore.save_local("index/faiss_index")
    print("___________________________________________________________")
    print("Converted CSV to Vector Successfully")
    print("___________________________________________________________")
except FileNotFoundError as e:
    print(f"Error: {e}")
