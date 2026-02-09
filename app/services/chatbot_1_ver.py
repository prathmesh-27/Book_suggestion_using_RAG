from langchain_ollama import OllamaLLM
from app.services.prompt_template import prompt
from app.services.rag import load_retriever

llm = OllamaLLM(model="llama3.2:1b",
                # device="cuda",
                # n_gpu_layers=3,          # only first 3 layers on GPU
                # max_gpu_memory="3.0G",   # limit VRAM usage
                # dtype="float16"
                )
chain = prompt | llm
retriever = load_retriever(k=8)


def get_response(query: str):
    docs = retriever.get_relevant_documents(query)
    for i, doc in enumerate(docs):
        print("---- DOC", i, "----")
        print(doc.page_content[:500])
    context = "\n\n".join([doc.page_content for doc in docs])
    response = chain.invoke({"context": context, "question": query})
    return response
