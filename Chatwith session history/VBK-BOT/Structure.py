import os

# Define the root directory for the project
root_dir = r"C:\Projects\ConversationalQA_Chatbot\Chatwith session history\VBK-BOT"

# Define folders to create
folders = [
    "handlers",
    "prompts",
    "db"
]

# Define files and their initial contents
files = {
    "handlers/__init__.py": "",
    "handlers/generic_handler.py": """def handle(message):
    return "This is the Generic Handler responding to: " + message
""",
    "handlers/appointment_handler.py": """def handle(message):
    return "This is the Appointment Handler responding to: " + message
""",
    "prompts/__init__.py": "",
    "prompts/conversation_prompt.py": """# Conversation prompt template goes here
""",
    "prompts/intent_detection_prompt.py": """# Placeholder for LangChain model integration

def detect_intent(message: str) -> str:
    message_lower = message.lower()
    if "book" in message_lower or "meeting" in message_lower or "schedule" in message_lower:
        return "appointment"
    elif "service" in message_lower or "offer" in message_lower or "price" in message_lower:
        return "generic"
    else:
        return "generic"
""",
    "db/__init__.py": "",
    "db/db_manager.py": """# Database manager code will go here
""",
    "session_manager.py": """# Code to manage session histories
""",
    "utils.py": """# Helper functions
""",
    "main.py": '''"""
Main entry point script
"""

from prompts.intent_detection_prompt import detect_intent
from handlers import generic_handler, appointment_handler

def route_intent(intent: str, message: str) -> str:
    if intent == "generic":
        return generic_handler.handle(message)
    elif intent == "appointment":
        return appointment_handler.handle(message)
    else:
        return f"No handler implemented for intent: [{intent}]"

def main():
    print("🤖 Welcome to VBK-BOT (type 'exit' to quit)\\n")
    while True:
        user_message = input("You: ")
        if user_message.lower() == "exit":
            print("Bot: Goodbye!")
            break

        intent = detect_intent(user_message)
        print(f"🔍 Detected Intent: [{intent}]")

        response = route_intent(intent, user_message)
        print("Bot:", response)
        print("-" * 50)

if __name__ == "__main__":
    main()
''',
    "streamlit_app.py": '''import streamlit as st
from prompts.intent_detection_prompt import detect_intent
from handlers import generic_handler, appointment_handler

st.title("💬 VBK Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.chat_history.append(("You", user_input))

    intent = detect_intent(user_input)

    if intent == "generic":
        reply = generic_handler.handle(user_input)
    elif intent == "appointment":
        reply = appointment_handler.handle(user_input)
    else:
        reply = f"Sorry, I don’t have a handler for intent: [{intent}]"

    st.session_state.chat_history.append(("Bot", reply))

for sender, msg in st.session_state.chat_history:
    with st.chat_message("user" if sender == "You" else "assistant"):
        st.write(msg)
''',
    "requirements.txt": """langchain
langchain_groq
python-dotenv
streamlit
""",
    ".env": """GROQ_API_KEY=your_api_key_here
"""
}

# Create the folder structure
for folder in folders:
    os.makedirs(os.path.join(root_dir, folder), exist_ok=True)

# Create files with initial content
for file_rel_path, content in files.items():
    file_path = os.path.join(root_dir, file_rel_path)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

"✅ Complete project structure and templates created successfully."
