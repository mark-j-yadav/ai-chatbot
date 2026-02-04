from openai import OpenAI
from config import OPENAI_API_KEY
from memory import get_history, save_message

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are a professional, friendly AI chatbot.
You reply clearly and helpfully.
"""

def get_ai_response(user_message: str) -> str:
    save_message("user", user_message)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *get_history()
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )

    reply = response.choices[0].message.content
    save_message("assistant", reply)

    return reply
