# 🤖 AI Chatbot – React + FastAPI + OpenAI

A full-stack **AI Chatbot application** built using **React (Frontend)**, **FastAPI (Backend)**, and **OpenAI GPT models**.  
This project is designed to demonstrate real-world AI integration, clean architecture, and modern UI/UX using Tailwind CSS.

---

## 🚀 Features

- ⚛️ Modern React frontend (Vite)
- 🎨 Tailwind CSS based SaaS-style UI
- 🤖 AI-powered chatbot using OpenAI
- 🧠 Context-aware chat memory
- 🌐 FastAPI REST backend
- 🔐 Secure environment variable usage
- 🔄 CORS enabled for frontend-backend communication
- 📱 Fully responsive design

---

## 🛠 Tech Stack

### Frontend
- React (Vite)
- Tailwind CSS
- JavaScript (ES6+)

### Backend
- Python
- FastAPI
- OpenAI API
- Uvicorn
- Python-dotenv

---



## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone git@github.com:mark-j-yadav/ai-chatbot.git
cd ai-chatbot
```

### 🐍 Backend Setup (FastAPI)
1. Create virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate virtual environment:
   ```bash
   venv\Scripts\activate   # Windows
   source venv/bin/activate # macOS/Linux
   ```
3. Install backend dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Create a `.env` file in the project root:
   ```bash
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
   ```
   ⚠️ Never commit `.env` to GitHub.
5. Run backend server:
   ```bash
   uvicorn backend.main:app --reload
   ```

Backend running at:
- http://127.0.0.1:8000  
- Swagger API Docs: http://127.0.0.1:8000/docs

### ⚛️ Frontend Setup (React + Tailwind)
```bash
cd fronted
npm install
npm run dev
```

Frontend running at:
- http://localhost:5173

---

## 🔄 API Usage
**Endpoint:** `POST /chat`

**Request Body:**
```json
{
  "message": "Hello AI"
}
```

**Response:**
```json
{
  "reply": "Hello! How can I help you today?"
}
```

---

## 🔐 Security Best Practices
- API key is stored in `.env`
- OpenAI key is never exposed to frontend
- `.env` is added to `.gitignore`
- Backend handles all AI communication

---

## 🧠 AI Configuration
You can customize AI behavior in `backend/config.py`:
- Model name
- Temperature
- Maximum chat history
- System prompt

---

## 🌟 Future Improvements
- 🌙 Dark mode
- 👤 User-based chat sessions
- ⏳ Streaming responses (typing effect)
- 🔐 Authentication (JWT)
- ☁️ Deployment (Render / Railway / Vercel)

---

## 👨‍💻 Author
Mark J Yadav  
Full-Stack Developer | AI Enthusiast
