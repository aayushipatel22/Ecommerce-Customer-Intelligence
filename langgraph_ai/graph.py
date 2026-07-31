from langgraph.graph import StateGraph, END

from langgraph_ai.state import ChatState
from langgraph_ai.retrieve import retrieve_context
from langgraph_ai.llm import llm


def generate_answer(state):
    """
    Generate the final answer using Gemini.
    """

    prompt = f"""
You are an AI Customer Intelligence Assistant.

Your task is to answer the user's question ONLY using the customer reviews provided below.

If the reviews do not contain enough information, say:
"I couldn't find enough information in the customer reviews."

=========================
Customer Reviews
=========================

{state["context"]}

=========================
User Question
=========================

{state["question"]}

=========================
Answer
=========================
"""

    # Call Gemini
    response = llm.invoke(prompt)

    # Handle different response formats
    if isinstance(response.content, str):
        answer = response.content

    elif isinstance(response.content, list):
        answer = ""

        for block in response.content:

            # Newer LangChain versions often return dictionaries
            if isinstance(block, dict):
                if block.get("type") == "text":
                    answer += block.get("text", "")

            # Sometimes blocks are objects
            elif hasattr(block, "text"):
                answer += block.text

            else:
                answer += str(block)

    else:
        answer = str(response.content)

    state["answer"] = answer.strip()

    return state


# -------------------------
# Build LangGraph
# -------------------------

builder = StateGraph(ChatState)

builder.add_node("Retrieve", retrieve_context)
builder.add_node("LLM", generate_answer)

builder.set_entry_point("Retrieve")

builder.add_edge("Retrieve", "LLM")
builder.add_edge("LLM", END)

graph = builder.compile()









# from langgraph.graph import StateGraph, END
# from langgraph_ai.state import ChatState
# from langgraph_ai.retrieve import retrieve_context
# from langgraph_ai.llm import llm

# def generate_answer(state):

#     prompt = f"""
# You are an AI assistant for an e-commerce company.

# Customer Reviews:

# {state["context"]}

# Question:

# {state["question"]}

# Answer based only on the reviews above.
# """
#     response = llm.invoke(prompt)

#     state["answer"] = response.content

#     return state

# builder = StateGraph(ChatState)

# builder.add_node("Retrieve", retrieve_context)

# builder.add_node("LLM", generate_answer)

# builder.set_entry_point("Retrieve")

# builder.add_edge("Retrieve", "LLM")

# builder.add_edge("LLM", END)

# graph = builder.compile()