# chatbot.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

genai.configure(api_key=api_key)

# Use the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash-latest')


def ask_bot(prompt):
    response = model.generate_content(prompt)

    if response and response.candidates:
        text_parts = response.candidates[0].content.parts
        full_text = ""
        for part in text_parts:
            if hasattr(part, 'text'):
                full_text += part.text + "\n"
        return full_text.strip()
    else:
        return "No response from model."
