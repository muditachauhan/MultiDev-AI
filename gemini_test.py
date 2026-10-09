import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain what an AI agent is in one simple sentence."
)

print(interaction.output_text)