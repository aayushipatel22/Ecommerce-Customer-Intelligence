# An embedding converts text into numbers (vectors). 

# Which Embedding Model? 
# We'll use a Hugging Face Sentence Transformer: all-MiniLM-L6-v2 
# Why? 
# Small (~90 MB), Fast, Free, Excellent for semantic search, Widely used

from sentence_transformers import SentenceTransformer

print("Loading Embedding Model...")

# loads a pretrained model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2" #This model was already trained by researchers at Microsoft using millions of sentences
)

print("Embedding Model Loaded Successfully!")

# We don't need training because we're using a pre-trained embedding model


# We use the pre-trained all-MiniLM-L6-v2 Sentence Transformer model, so no training is required. 
# The model has already learned semantic relationships from millions of sentences. In our project, 
# we only perform inference by converting review text into vector embeddings for semantic search.