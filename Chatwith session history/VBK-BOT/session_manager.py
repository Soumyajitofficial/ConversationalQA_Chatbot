# Code to manage session histories
from langchain.memory import ChatMessageHistory
from langchain.schema import BaseChatMessageHistory
from langchain.schema.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory

# In-memory storage for sessions
store = {}

# Function to get or create session-specific message history
def get_session_history(sessionID: str) -> BaseChatMessageHistory:
    if sessionID not in store:
        store[sessionID] = ChatMessageHistory()
    return store[sessionID]
