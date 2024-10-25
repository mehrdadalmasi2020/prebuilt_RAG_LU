from transformers import AutoTokenizer, AutoModelForCausalLM

class LLMGenerator:
    def __init__(self, model_name="gpt2", token=None):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=token)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=token)

    def generate_text(self, prompt, max_new_tokens=100):
        inputs = self.tokenizer(prompt, return_tensors="pt")

        # Generate text using max_new_tokens instead of max_length
        outputs = self.model.generate(
            inputs['input_ids'],
            max_new_tokens=max_new_tokens,  # Only specify the number of new tokens to generate
            pad_token_id=self.tokenizer.eos_token_id  # Use eos_token_id as the pad token
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
if __name__ == "__main__":
    llm_gen = LLMGenerator(model_name="mistralai/Mistral-7B-v0.3")
    prompt = "Tell me about AI and its applications in healthy food and better living."
    generated_text = llm_gen.generate_text(prompt)
    print("Generated Text:", generated_text)
