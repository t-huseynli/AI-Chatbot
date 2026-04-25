# 🤖 AI Chatbot (FastAPI + Ollama)

A simple AI chatbot built with **FastAPI** and **Ollama (Gemma model)** that supports **conversation memory** and a modern web interface.

---

## 🚀 Features

* 💬 Chat with AI (Gemma model via Ollama)
* 🧠 Short-term memory (remembers recent messages)
* ⚡ FastAPI backend
* 🌐 Simple modern frontend (HTML/CSS/JS)
* 🔄 Real-time interaction

---

## 🛠️ Tech Stack

* Backend: FastAPI (Python)
* AI Model: Ollama (Gemma)
* Frontend: HTML, CSS, JavaScript
* HTTP Requests: requests

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-chatbot.git
cd ai-chatbot
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install and run Ollama

Download Ollama:
👉 https://ollama.com

Run the model:

```bash
ollama run gemma
```

Make sure Ollama is running on:

```
http://localhost:11434
```

---

### 5. Start FastAPI server

```bash
uvicorn main:app --reload
```

---

### 6. Open the frontend

Open your HTML file in browser:

```
index.html
```

---

## 🧠 How Memory Works

This chatbot implements **short-term memory** by storing recent messages in a list:

```python
chat_history = []
```

On each request:

1. User message is added to history
2. Last N messages are selected
3. They are sent to the model as context

Example prompt:

```
User: Hello
Assistant: Hi!
User: What is my name?
Assistant:
```

This allows the model to respond with context.

---

## ⚠️ Limitations

* Memory resets when server restarts
* No user authentication (shared memory)
* Limited to MAX_HISTORY value messages stored in memory

---

## 🔮 Future Improvements

* 🗄️ PostgreSQL database for persistent memory
* 👤 User accounts & sessions
* 🧠 Long-term memory (vector embeddings)
* 🎨 React frontend
* ⚡ Streaming responses

---


## 👨‍💻 Author

Tahir Huseynli

---

## 📄 License

MIT License
