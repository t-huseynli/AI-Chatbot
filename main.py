from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

chat_history = []


MAX_HISTORY = 6

@app.post("/chat")
def chat(req: ChatRequest):

    chat_history.append(f"User: {req.message}")

    recent_history = chat_history[-MAX_HISTORY:]

    prompt = "\n".join(recent_history) + "\nAssistant:"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma4",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    bot_reply = data.get("response", "No response field found")

    chat_history.append(f"Assistant: {bot_reply}")

    return {
        "response": bot_reply
    }