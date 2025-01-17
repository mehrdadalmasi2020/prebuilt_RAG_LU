# prebuilt_RAG_LU

## Overview
`prebuilt_RAG_LU` is a Python library designed to facilitate **Retrieval-Augmented Generation (RAG)** workflows. It provides a streamlined interface for embedding generation, vector-based document retrieval using **ChromaDB**, and integration with popular language models (LLMs) to generate human-readable responses based on retrieved documents.

### Features:
- **Embedding Generation**: Supports multiple pre-trained models from Hugging Face for generating vector embeddings, including multilingual and lightweight models.
- **Vector Database Management**: Store, query, and delete vector-based document embeddings using **ChromaDB**.
- **LLM Integration**: Generate text responses using state-of-the-art models like **GPT-2**, **T5**, and the high-performance **Mistral-7B-v0.3**.
**Note**: Using the Mistral model (`mistralai/Mistral-7B-v0.3`) requires a GPU with at least **30GB of memory** for optimal performance.

## Installation
To install the required dependencies, use the following commands:

```bash
pip install transformers chromadb

```

## Usage

Here is how you can use `prebuilt_RAG_LU` for embedding generation, document retrieval, and final response generation using LLMs.

### 1. Embedding Generation
Use the `EmbeddingGenerator` class to generate vector embeddings for text. You can choose from several pre-trained models:

```python 
from prebuilt_RAG_LU import EmbeddingGenerator, VectorDatabase, LLMGenerator, Config

# Initialize configuration
config = Config()

# Initialize components using values from the config instance
embedding_generator = EmbeddingGenerator(model_name="xlm-roberta-large")  # or another embedding model


```
### Available Models for Embedding Generation

#### Lightweight Models:
- `distilbert-base-uncased`
- `microsoft/MiniLM-L12-H384-uncased`

#### Heavyweight Models:
- `bert-base-uncased`
- `sentence-transformers/all-MiniLM-L6-v2`

#### Multilingual Models:
- `xlm-roberta-large` (1024 dimensions)
- `bert-base-multilingual-cased`
- `sentence-transformers/LaBSE`

---

### 2. Vector Database Management
Once you have the embeddings, you can store and manage them in ChromaDB using the `VectorDatabase` class:

```python

vector_db = VectorDatabase()
llm_generator = LLMGenerator(model_name=config.model_name, token=config.user_token)

# 1. Insert Documents into the Vector Database
documents = [
    {"id": "doc1", "text": "AI is revolutionizing the food industry by analyzing nutritional data and recommending healthier meal options tailored to individual dietary needs. This helps people make better food choices."},
    {"id": "doc2", "text": "Artificial Intelligence enables personalized nutrition plans based on health data such as age, weight, and medical history, ensuring individuals receive optimal nutrients for a balanced, healthy lifestyle."},
    {"id": "doc3", "text": "AI applications in healthcare extend to monitoring dietary habits and suggesting improvements, helping people adopt healthier eating patterns, reduce stress, and improve overall quality of life."},
    {"id": "doc4", "text": "With AI-driven apps, users can track their calorie intake, monitor nutrient levels, and receive real-time suggestions for healthier food alternatives, helping them achieve their fitness and health goals."},
    {"id": "doc5", "text": "AI-powered health assistants can provide instant feedback on meal choices and suggest healthier recipes, helping individuals maintain a balanced diet while avoiding unhealthy foods."},
    {"id": "doc6", "text": "AI in food science is being used to develop plant-based food alternatives that mimic meat but offer healthier options for consumers, reducing reliance on animal-based products and promoting sustainability."},
    {"id": "doc7", "text": "Through AI, food companies are able to optimize their product lines by analyzing consumer data and creating healthier snack and meal options that cater to different dietary preferences and health concerns."},
    {"id": "doc8", "text": "AI-enabled wearable devices can track a person's activity levels, heart rate, and caloric burn, then adjust food recommendations accordingly, ensuring the body receives the energy it needs to function optimally."},
    {"id": "doc9", "text": "AI helps detect harmful ingredients in processed foods by analyzing chemical compositions and flagging unhealthy additives, empowering consumers to make more informed food choices."},
    {"id": "doc10", "text": "AI can predict future health risks by analyzing a person's diet and lifestyle patterns, then recommend proactive dietary changes that reduce the risk of diseases such as diabetes and heart disease."}
]


# Generate embeddings for the documents and upsert them into the vector database
doc_ids = [doc["id"] for doc in documents]
doc_embeddings = [embedding_generator.get_embedding(doc["text"]) for doc in documents]
doc_metadatas = [{"content": doc["text"]} for doc in documents]

vector_db.upsert_documents(ids=doc_ids, embeddings=doc_embeddings, metadatas=doc_metadatas)

# Embedding Generation for the Query
query_text = "How does AI contribute to healthy food choices and living a better life?"
query_embedding = embedding_generator.get_embedding(query_text)

# Document Retrieval based on the Query
retrieved_docs = vector_db.query_documents(query_embedding, n_results=3)
context = " ".join([doc["metadata"]["content"] for doc in retrieved_docs])

```
### Key Methods

- `upsert_documents(ids, embeddings, metadatas)`: Inserts or updates documents in the vector database.

- `query_documents(query_embedding, n_results=2)`: Retrieves the most similar documents based on the input embedding.

- `delete_document(doc_id)`: Deletes a document from the vector database.

### 3. LLM-Based Result Generation
After retrieving the relevant documents, use an LLM to generate a final response. The `LLMGenerator` class integrates several popular language models, including `Mistral-7B-v0.3`.

```python
# LLM-Based Generation with Retrieved Context
final_prompt = f"Based on the following information: {context}. Answer the question: {query_text}"
generated_text = llm_generator.generate_text(final_prompt)

print("Generated Text:", generated_text)

```

### Available LLM Models for Text Generation

- **GPT-2** (lightweight): `gpt2`
- **EleutherAI GPT-Neo 1.3B** (medium scale): `EleutherAI/gpt-neo-1.3B`
- **Meta OPT 1.3B** (medium scale): `facebook/opt-1.3b`
- **Google Flan-T5 Base** (T5 variant): `google/flan-t5-base`
- **Mistral-7B-v0.3** (high-performance): `mistralai/Mistral-7B-v0.3`

---

## Full RAG Workflow Example
Here is how you can combine embedding generation, vector database management, and LLM-based result generation into a complete RAG workflow.

```python

from prebuilt_RAG_LU import EmbeddingGenerator, VectorDatabase, LLMGenerator, Config

# Initialize configuration
config = Config()

# Initialize components using values from the config instance
embedding_generator = EmbeddingGenerator(model_name="xlm-roberta-large")  # or another embedding model
vector_db = VectorDatabase()
llm_generator = LLMGenerator(model_name=config.model_name, token=config.user_token)

# 1. Insert Documents into the Vector Database
# Example documents to insert
documents = [
    {"id": "doc1", "text": "AI is revolutionizing the food industry by analyzing nutritional data and recommending healthier meal options tailored to individual dietary needs. This helps people make better food choices."},
    {"id": "doc2", "text": "Artificial Intelligence enables personalized nutrition plans based on health data such as age, weight, and medical history, ensuring individuals receive optimal nutrients for a balanced, healthy lifestyle."},
    {"id": "doc3", "text": "AI applications in healthcare extend to monitoring dietary habits and suggesting improvements, helping people adopt healthier eating patterns, reduce stress, and improve overall quality of life."},
    {"id": "doc4", "text": "With AI-driven apps, users can track their calorie intake, monitor nutrient levels, and receive real-time suggestions for healthier food alternatives, helping them achieve their fitness and health goals."},
    {"id": "doc5", "text": "AI-powered health assistants can provide instant feedback on meal choices and suggest healthier recipes, helping individuals maintain a balanced diet while avoiding unhealthy foods."},
    {"id": "doc6", "text": "AI in food science is being used to develop plant-based food alternatives that mimic meat but offer healthier options for consumers, reducing reliance on animal-based products and promoting sustainability."},
    {"id": "doc7", "text": "Through AI, food companies are able to optimize their product lines by analyzing consumer data and creating healthier snack and meal options that cater to different dietary preferences and health concerns."},
    {"id": "doc8", "text": "AI-enabled wearable devices can track a person's activity levels, heart rate, and caloric burn, then adjust food recommendations accordingly, ensuring the body receives the energy it needs to function optimally."},
    {"id": "doc9", "text": "AI helps detect harmful ingredients in processed foods by analyzing chemical compositions and flagging unhealthy additives, empowering consumers to make more informed food choices."},
    {"id": "doc10", "text": "AI can predict future health risks by analyzing a person's diet and lifestyle patterns, then recommend proactive dietary changes that reduce the risk of diseases such as diabetes and heart disease."}
]

# Generate embeddings for the documents and upsert them into the vector database
doc_ids = [doc["id"] for doc in documents]
doc_embeddings = [embedding_generator.get_embedding(doc["text"]) for doc in documents]
doc_metadatas = [{"content": doc["text"]} for doc in documents]

vector_db.upsert_documents(ids=doc_ids, embeddings=doc_embeddings, metadatas=doc_metadatas)

# 2. Embedding Generation for the Query
query_text = "How does AI contribute to healthy food choices and living a better life?"
query_embedding = embedding_generator.get_embedding(query_text)

# 3. Document Retrieval based on the Query
retrieved_docs = vector_db.query_documents(query_embedding, n_results=3)
context = " ".join([doc["metadata"]["content"] for doc in retrieved_docs])

# 4. LLM-Based Generation with Retrieved Context
final_prompt = f"Based on the following information: {context}. Answer the question: {query_text}"
generated_text = llm_generator.generate_text(final_prompt)

print("Generated Text:", generated_text)

```
## Configuration

The library allows flexible configuration of models for embedding generation and text generation. You can modify the model selection based on your specific needs.

### Embedding Models:

- **Lightweight**:
  - `distilbert-base-uncased`
  - `microsoft/MiniLM-L12-H384-uncased`

- **Heavyweight**:
  - `bert-base-uncased`
  - `sentence-transformers/all-MiniLM-L6-v2`

- **Multilingual**:
  - `xlm-roberta-large`
  - `bert-base-multilingual-cased`
  - `sentence-transformers/LaBSE`

### LLM Models:

- **GPT-2**: `gpt2`
- **GPT-Neo 1.3B**: `EleutherAI/gpt-neo-1.3B`
- **OPT 1.3B**: `facebook/opt-1.3b`
- **Flan-T5 Base**: `google/flan-t5-base`
- **Mistral-7B-v0.3**: `mistralai/Mistral-7B-v0.3`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



