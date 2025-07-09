import os

# Root directory
root_dir = r"C:\Projects\ConversationalQA_Chatbot\Chatwith session history\VBK-BOT"

# Folder structure to create
folders = [
    "handlers",
    "prompts",
    "db",
]

# Files with starter content
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
    "prompts/intent_detection_prompt.py": """# Intent detection prompt template goes here
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

def main():
    print("VBK-BOT project is set up!")

if __name__ == "__main__":
    main()
''',
    "requirements.txt": """langchain
langchain_groq
python-dotenv
""",
    ".env": """GROQ_API_KEY=your_api_key_here
"""
}

# Create folders
for folder in folders:
    path = os.path.join(root_dir, folder)
    os.makedirs(path, exist_ok=True)

# Create files
for file_rel_path, content in files.items():
    file_path = os.path.join(root_dir, file_rel_path)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Project structure created successfully at:", root_dir)
