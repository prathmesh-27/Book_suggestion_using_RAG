from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the following Question

Here is the history: {context}

Question: {question}

Answer:

"""


model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_convo():
    context = ""
    print("Hello Welcome to my AI chatbot. Type exit to quit")
    while True:
        user_input = input("YOU: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": {user_input}})
        print("BOT: ", result)
        context = f"\nUser: {user_input}\nAI: {result}"


def ask_ollama(context, question):
    return chain.invoke({
        "context": context,
        "question": question
    })


if __name__ == "__main__":
    handle_convo()
