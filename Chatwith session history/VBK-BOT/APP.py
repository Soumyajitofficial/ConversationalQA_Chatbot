# APP.py

import streamlit as st
from session_manager import get_session_history
from prompts.intent_detection_prompt import detect_intent
#from handlers.appointment_handler import handle_appointment
#from handlers.generic_handler import handle_generic

# Streamlit UI setup
st.set_page_config(page_title="VBK Bot", layout="wide")
st.title("📊 Virtuous Bookkeeping Assistant")

# Session setup
config1_input = st.text_input("Enter config (example: config1 = {\"configurable\": {\"session_id\": \"s1\"}}):", "")
try:
    config1 = eval(config1_input) if config1_input else {"configurable": {"session_id": "default"}}
    session_id = config1["configurable"]["session_id"]
except:
    st.error("⚠️ Invalid config. Please enter a valid Python dictionary with session_id.")
    session_id = "default"

# Get session-specific message history
chat_history = get_session_history(session_id)

# Chat interface
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        # Add user message to chat history
        chat_history.add_user_message(user_input)

        # Detect intent
        intent = detect_intent(user_input)

        # Handle intent
        if intent == "[appointment]":
            response = handle_appointment(user_input)
        elif intent == "[generic]":
            response = handle_generic(user_input)
        elif intent == "[handoff]":
            response = "👩‍💼 Please wait while we connect you to a team member."
        else:
            response = f"⚠️ No handler implemented for intent: {intent}"

        # Add assistant message to chat history
        chat_history.add_ai_message(response)

# Display conversation history
if chat_history.messages:
    st.subheader("Conversation History")
    for msg in chat_history.messages:
        role = "You" if msg.type == "human" else "Bot"
        st.markdown(f"**{role}:** {msg.content}")
