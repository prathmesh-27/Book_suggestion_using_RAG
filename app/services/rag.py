import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

PROJECT_ROOT = os.environ.get("PROJECT_ROOT")

FAISS_INDEX_PATH = os.path.join(
    PROJECT_ROOT,
    "index",
    "faiss_index"
)


def load_retriever(index_path=FAISS_INDEX_PATH, k=3):
    # embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    vectorstore = FAISS.load_local(
        index_path, embedding_model, allow_dangerous_deserialization=True)

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": k, "fetch_k": 25, "lambda_mult": 0.7}
    )

    return retriever
