import streamlit as st
from prompts.intent_detection_prompt import detect_intent
from handlers import generic_handler, appointment_handler

# Optional: You can expand this with more handlers
def route_intent(intent: str, message: str) -> str:
    if intent == "[generic]":
        return generic_handler.handle(message)
    elif intent == "appointment":
        return appointment_handler.handle(message)
    else:
        return f"⚠️ No handler implemented for intent: [{intent}]"

# Streamlit page setup
st.set_page_config(page_title="VBK Chatbot", page_icon="💬")
st.title("💬 VBK Virtual Assistant")
st.caption("Your accounting-friendly AI assistant 💼")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Handle user input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Show user message
    st.session_state.chat_history.append(("You", user_input))

    # Intent detection
    intent = detect_intent(user_input)

    # Route to appropriate handler
    reply = route_intent(intent, user_input)

    # Show bot response
    st.session_state.chat_history.append(("Bot", reply))

# Display chat history
for sender, msg in st.session_state.chat_history:
    with st.chat_message("user" if sender == "You" else "assistant"):
        st.write(msg)