from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def load_retriever(index_path="../index/faiss_index", k=3):
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(
        index_path, embedding_model, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": k})
    return retriever
