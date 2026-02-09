from langchain_core.prompts import ChatPromptTemplate

template = template = """
You are a book assistant.

Rules:
- Use ONLY the context.
- If the answer is not clearly present in the context, reply: "Not found in dataset."
- Do not guess.
- Keep the answer short.

Context:
{context}

Question: {question}

Answer:
"""


prompt = ChatPromptTemplate.from_template(template)
