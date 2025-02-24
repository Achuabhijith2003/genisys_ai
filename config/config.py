import os
from dotenv import load_dotenv

load_dotenv()

# openai
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# memory
MAX_MEMORY_N = int(os.getenv("MAX_MEMORY_N"))
MEMORY_FILE = os.getenv("MEMORY_FILE")

# weather
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

# listener
Listenkey = True
SLEEP_N = 3
SLEEP_COUNT = 0