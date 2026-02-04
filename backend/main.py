from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_ai_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Chatbot Backend")

# CORS (React ke liye mandatory)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.get("/")
def health_check():
    return {"status": "Backend running 🚀"}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    reply = get_ai_response(req.message)
    return {"reply": reply}
