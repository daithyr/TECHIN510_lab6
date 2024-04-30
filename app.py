# Import necessary libraries
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def send_prompt(prompt_text):
    try:
        # Sending a request to the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-002",  # You can choose different models
            prompt=prompt_text,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Direct Prompt
direct_prompt = "Explain the theory of relativity."
print("Direct Prompt Response:", send_prompt(direct_prompt))

# Few-shot Learning Example
few_shot_prompt = """Q: What is photosynthesis?
A: Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods from carbon dioxide and water. Photosynthesis in plants generally involves the green pigment chlorophyll and generates oxygen as a byproduct.

Q: What is quantum entanglement?
A: """
print("Few-shot Prompt Response:", send_prompt(few_shot_prompt))

# Zero-shot Technique
zero_shot_prompt = "Write a poem about the ocean."
print("Zero-shot Prompt Response:", send_prompt(zero_shot_prompt))
