from qdrant_db.search_vectors import search as semantic_search
from elasticsearch_db.search_documents import search as keyword_search

def retrieve_context(state):

    question = state["question"]

    semantic_results = semantic_search(question)

    keyword_results = keyword_search(question)

    context = []

    for item in semantic_results:
        context.append(item["review_text"])

    for item in keyword_results:
        context.append(item["review_text"])

    state["context"] = "\n".join(context)

    return state