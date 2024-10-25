# prebuilt_RAG_LU/config.py

class Config:
    def __init__(self):
        self.available_models = {
            "1": "gpt2",
            "2": "EleutherAI/gpt-neo-1.3B",
            "3": "facebook/opt-1.3b",
            "4": "google/flan-t5-base",
            "5": "mistralai/Mistral-7B-v0.3"
        }
        self.model_name = self.get_model_choice()
        self.user_token = self.get_user_token(self.model_name)

    def get_model_choice(self):
        """Prompt the user to select a model for text generation."""
        print("Please select a model for text generation:")
        for key, model_name in self.available_models.items():
            print(f"{key}: {model_name}")
        choice = input("Enter the number of your model choice: ")
        return self.available_models.get(choice, "gpt2")  # Default to 'gpt2' if choice is invalid

    def get_user_token(self, model_name):
        """Prompt for a Hugging Face API token if needed for gated models."""
        if model_name == "mistralai/Mistral-7B-v0.3":
            return input("Enter your Hugging Face API token for Mistral-7B-v0.3: ")
        return None
