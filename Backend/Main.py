import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentResponse

load_dotenv()

# fetch the key from .env
key = os.getenv("GEMINI_API_KEY")

# error handling for missing API key
if not key:
    raise ValueError("GEMINI_API_KEY not found! Check .env file.")

# Create the client
# Note: the client will auto-detect the API key from the environment variable
client = genai.Client(api_key=key)

input_text = input("How can I help today? ")

# Streamin generation
stream = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=input_text+"Keep your answer concise and to the point. Be conversational and engaging, but avoid unnecessary details. Focus on providing clear and direct responses to the user's query.",
)

print("Incoming NeuroText", end="", flush=True)

# Simulate loading/thinking animation
for _ in range(6):
    time.sleep(0.3)
    print(".", end="", flush=True)
print("\n")

# Simulate typing animation
for chunk in stream:
    if chunk.text:
        for char in chunk.text:
            print(char, end="", flush=True)
            time.sleep(0.015)