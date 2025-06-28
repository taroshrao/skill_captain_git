from transformers import AutoTokenizer, AutoModel
import torch

# Load model
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

# Encode sentence
sentence = "I love learning about AI and coding at skill captain."
inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)

# Get embeddings
with torch.no_grad():
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)  # Mean pooling

print("Vector embedding shape:", embeddings.shape)
print("Vector sample:", embeddings[0][:5])  # Print first 5 values

#output: Vector embedding shape: torch.Size([1, 384])
#output: Vector sample: tensor([-0.2343, -0.4282,  0.0363, -0.0334,  0.2762])
