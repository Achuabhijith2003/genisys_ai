import json
import os
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage
from config import config

MEMORY_FILE = config.MEMORY_FILE

# Function to load chat history and convert to LangChain format
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            history = json.load(file).get("chat_history", [])[-config.MAX_MEMORY_N:]

            # Convert JSON objects back to LangChain messages
            messages = []
            for msg in history:
                if msg["role"] == "user":
                    messages.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":  # Fixed the incorrect role
                    messages.append(AIMessage(content=msg["content"]))
            return messages
    return []

# Function to save only the last MAX_MEMORY_N messages (JSON-safe)
def save_memory(history):
    json_safe_history = [
        {"role": "user" if isinstance(msg, HumanMessage) else "assistant", "content": msg.content}
        for msg in history[-config.MAX_MEMORY_N:]
    ]
    
    with open(MEMORY_FILE, "w") as file:
        json.dump({"chat_history": json_safe_history}, file, indent=4)

# Initialize memory
memory = ConversationBufferMemory(return_messages=True)

# Load previous messages into memory
previous_messages = load_memory()
for msg in previous_messages:
    memory.chat_memory.add_message(msg)
