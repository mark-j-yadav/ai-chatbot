chat_history = []

MAX_HISTORY = 10  # last 10 messages only

def save_message(role: str, content: str):
    chat_history.append({"role": role, "content": content})

    if len(chat_history) > MAX_HISTORY:
        chat_history.pop(0)

def get_history():
    return chat_history
