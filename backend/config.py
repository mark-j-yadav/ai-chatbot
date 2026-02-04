import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# =========================
# API KEYS
# =========================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# =========================
# APP SETTINGS
# =========================
APP_NAME = "AI Chatbot Backend"
APP_VERSION = "1.0.0"

# =========================
# AI SETTINGS
# =========================
AI_MODEL = "gpt-4o-mini"
AI_TEMPERATURE = 0.7
MAX_HISTORY = 10
