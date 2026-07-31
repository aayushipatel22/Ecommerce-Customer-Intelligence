# from embeddings.embedding_model import embedding_model

# print("Model Loaded Successfully!")




# from qdrant_db.qdrant_client import client

# print(client.get_collections())






# from qdrant_db.qdrant_client import client
# import inspect

# print(inspect.signature(client.query_points))













# from embeddings.embedding_model import embedding_model

# print("Model Loaded!")

# vector = embedding_model.encode("camera quality")

# print(len(vector))
# print(vector[:5])













# from qdrant_db.qdrant_client import client

# collection_info = client.get_collection("customer_reviews")

# print(collection_info)
















# from qdrant_db.qdrant_client import client
# from embeddings.embedding_model import embedding_model

# query = "camera quality"

# vector = embedding_model.encode(query).tolist()

# response = client.query_points(
#     collection_name="customer_reviews",
#     query=vector,
#     limit=3
# )

# print(response)






# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# for model in client.models.list():
#     print(model.name)










# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# llm = ChatGoogleGenerativeAI(
#     model="gemini-flash-latest",
#     google_api_key=os.getenv("GEMINI_API_KEY"),
#     temperature=0.3,
# )

# response = llm.invoke("Hello! Tell me your name.")

# print(response.content)