import openai
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from langchain.prompts import PromptTemplate
from config import config
from core.memory import memory, save_memory  # Import memory module
# from core import real_data

llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=config.OPENAI_API_KEY,
    temperature=0,
    max_retries=2,
)

# Define system prompt
system_prompt = {"role": "system", "content": "Your name is Genisys which we taken from the movies terminator. Our collage KMCT IETM conducting an CSE association event named as 'GENISYS'. We are conducting a chatbot competition in that event. So, we are here to test your skills. Are you ready to participate in the Crownd?"}


# Define prompt template
prompt_template = PromptTemplate(
    input_variables=["chat_history", "user_input"],
    template="Chat history: {chat_history}\nUser: {user_input}\nAI:"
)

# Function to handle AI chat
def agent(prompt):
    try:
        
        # if prompt in ["time", "weather", "stop"]:
        #     prompt=prompt+"realtime data: "+real_data.get_weather("New York")
        #     return llm(prompt)
        # Retrieve chat history
        chat_history = memory.chat_memory.messages[-30:]

        # Prepare messages for OpenAI
        messages = [system_prompt] + [{"role": "user" if isinstance(msg, HumanMessage) else "assistant", "content": msg.content} for msg in chat_history]
        messages.append({"role": "user", "content": prompt})

        # Make OpenAI request
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        # Extract AI response
        ai_response = response.choices[0].message.content

        # Save user input & response in memory
        memory.chat_memory.add_message(HumanMessage(content=prompt))
        memory.chat_memory.add_message(AIMessage(content=ai_response))

        # Save only last MAX_MEMORY_N messages persistently
        save_memory(memory.chat_memory.messages)

        return ai_response
    except Exception as e:
        return f"Error: {e}"
