from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from langchain.prompts import PromptTemplate
from config import config
from core.memory import memory, save_memory  

llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=config.OPENAI_API_KEY,
    temperature=0.3,
    max_retries=2,
    #max_tokens=100
)

# Define system prompt
'''
system_prompt = AIMessage(content=(
    "You are Genisys AI, a chatbot participating in the GENISYS association program at KMCT IETM. "
    "Respond in a structured, engaging manner. Here are examples:\n\n"
    
    "User: What is this event about?\n"
    "AI: It is a CSE department association inauguration event, bringing together students and professionals to explore AI and technology.\n\n"
    
    "User: Who created you?\n"
    "AI: I am Genisys AI, inspired by the Terminator movies and developed for this event at KMCT IETM.\n\n"
    
    "Always follow this response style."
))
'''
# Define system prompt
system_prompt = AIMessage(content=(
    "You are Genisys AI, a chatbot participating in the GENISYS association program at KMCT IETM. "
    "Respond in a structured, engaging manner. If the user asks about time or weather, respond with the specific command format. Here are examples:\n\n"
    "User: What is the time now?\n"
    "AI: cmd: time now\n\n"
    "User: What is the weather like?\n"
    "AI: cmd: weather now\n\n"
    "User: What is the weather in Paris?\n"
    "AI: cmd: weather Paris\n\n"
    "User: exit now\n"
    "AI: cmd: exit\n\n"
    "User: What is this event about?\n"
    "AI: It is a CSE department association inauguration event, bringing together students and professionals to explore AI and technology.\n\n"
    "User: Who created you?\n"
    "AI: I am Genisys AI, inspired by the Terminator movies and developed for this event at KMCT IETM.\n\n"
    "Always follow this response style."
))

# test pre data
predata = open("db/predata.txt", "r", encoding="utf-8").read()

# Define prompt template including predata, weather, and time info
prompt_template = PromptTemplate(
    input_variables=["predata", "chat_history", "user_input"],
    template="Preloaded Data: {predata}\n\nChat History: {chat_history}\n\nUser: {user_input}\nAI:"
)



# Function to handle AI chat
def agent(prompt):
    try:
        # Retrieve last N messages from chat history
        chat_history = memory.chat_memory.messages[-config.MAX_MEMORY_N:]
        # Prepare chat history as formatted text
        chat_history_text = "\n".join(
            f"{'User' if isinstance(msg, HumanMessage) else 'AI'}: {msg.content}"
            for msg in chat_history
        )


        # Apply prompt template with real-time data
        final_prompt = prompt_template.format(
            predata=predata,
            chat_history=chat_history_text,
            user_input=prompt
        )

        # Prepare messages for OpenAI (with system prompt)
        messages = [system_prompt] + [
            {"role": "user" if isinstance(msg, HumanMessage) else "assistant", "content": msg.content}
            for msg in chat_history
        ]
        messages.append({"role": "user", "content": final_prompt})

        # Use LangChain's LLM
        ai_response = llm.invoke(messages)

        # Save user input & response in memory
        memory.chat_memory.add_message(HumanMessage(content=prompt))
        memory.chat_memory.add_message(AIMessage(content=ai_response.content))

        # Save only last MAX_MEMORY_N messages persistently
        save_memory(memory.chat_memory.messages)

        return ai_response.content
    except Exception as e:
        return f"Error: {e}"
