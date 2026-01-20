from langchain_core.prompts import ChatPromptTemplate

template = """
You are a helpful book assistant.

Answer the user's question using only the context below.

Context:
{context}

Question: {question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)
