from typing import TypedDict

class ChatState(TypedDict):
    question: str
    context: str
    answer: str

# LangGraph passes information between nodes using a state.