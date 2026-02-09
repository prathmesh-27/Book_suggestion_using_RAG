# Book Recommendation Chatbot Using RAG (LangChain + Ollama)

It is a minimal **terminal-based AI chatbot** built using **LangChain** and **Ollama**.  
It runs locally using the `llama3.2:1b` model and keeps basic conversation context during a session.

Clean, simple, and easy to extend.

---

## Current Features
- Command-line chatbot
- Uses LangChain prompt chaining
- Runs fully locally with Ollama
- Maintains conversation history per session
- It has Beginner-friendly structure

---

## Dataset

The dataset used in this project is the **CMU Book Summary Dataset**, which provides structured book metadata along with human-written summaries.


## 🛠 Requirements
- Python **3.10+**
- **Ollama** installed
- Ollama model: `llama3.2:1b` # I used this due to my machine limitation

Python dependencies:

Install dependencies using

```bash
pip install -r requirements. txt
```

## Installation

Clone the repository:
```bash
git clone https://github.com/prathmesh-27/Book_suggestion_using_RAG
cd Book_suggestion_using_RAG
```
Pull the `llama3.2:1b` model

```bash
ollama pull llama3.2:1b.
```

---

## How to Run

Run the Scripts in this Order

```bash 
python data_preprocessing\clean_book_data.py
```

```bash 
python build_index.py
```

```bash 
python run.py
```
---

<!-- ## Future Scope

- Persistent memory
- Web or API interface
- Streaming responses -->