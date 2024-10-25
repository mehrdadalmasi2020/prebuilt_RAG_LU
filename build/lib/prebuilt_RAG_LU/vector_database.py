import chromadb
from chromadb.errors import UniqueConstraintError

class VectorDatabase:
    def __init__(self, collection_name="documents"):
        # Initialize the Chroma client
        self.client = chromadb.Client()

        # Try to create the collection, and if it exists, catch the error and retrieve it
        try:
            self.collection = self.client.create_collection(collection_name)
        except UniqueConstraintError:
            # If the collection already exists, just get the existing collection
            print(f"Collection '{collection_name}' already exists. Retrieving it instead.")
            self.collection = self.client.get_collection(collection_name)

    def upsert_documents(self, ids, embeddings, metadatas):
        # Upsert documents into the collection
        self.collection.upsert(ids=ids, embeddings=embeddings, metadatas=metadatas)
        print("Documents upserted successfully.")

    def query_documents(self, query_embedding, n_results=2):
        # Query the collection for the most similar documents
        query_results = self.collection.query(query_embeddings=[query_embedding], n_results=n_results)
        results = []
        for i, doc_id in enumerate(query_results.get('ids', [[]])[0]):
            results.append({
                "id": doc_id,
                "metadata": query_results.get('metadatas', [[]])[0][i],
                "distance": query_results.get('distances', [[]])[0][i]
            })
        return results

    def delete_document(self, doc_id):
        # Delete a document by its ID
        self.collection.delete(ids=[doc_id])
        print(f"Document {doc_id} deleted successfully.")
