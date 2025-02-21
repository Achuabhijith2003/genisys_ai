import os
from dotenv import load_dotenv

load_dotenv()

# openai
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# memory
MAX_MEMORY_N = int(os.getenv("MAX_MEMORY_N"))
MEMORY_FILE = os.getenv("MEMORY_FILE")

# listener
Listenkey = True