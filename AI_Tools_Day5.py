from sentence_transformers import SentenceTransformer, util

# Load pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Our sentences
sentence_a = "I enjoy learning python."
sentence_b = "I love coding in Java."

# Get embeddings
embedding_a = model.encode(sentence_a, convert_to_tensor=True)
embedding_b = model.encode(sentence_b, convert_to_tensor=True)

# Cosine similarity
cosine_sim = util.pytorch_cos_sim(embedding_a, embedding_b)

print(f"Cosine similarity: {cosine_sim.item():.2f}")

#output Cosine similarity: 0.48
