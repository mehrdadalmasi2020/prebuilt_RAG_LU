from transformers import AutoTokenizer, AutoModel
import torch

class EmbeddingGenerator:
    def __init__(self, model_name="xlm-roberta-large"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def get_embedding(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
        return embedding
