# chatbot.py
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyA0Xi13r8ww8DcW5BkiDbBn_JYdaxAD034")  # Replace with your actual API key

# Use the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def ask_bot(prompt):
    response = model.generate_content(prompt)
    
    # Safely extract all text parts
    if response and response.candidates:
        text_parts = response.candidates[0].content.parts
        full_text = ""
        for part in text_parts:
            if hasattr(part, 'text'):
                full_text += part.text + "\n"  # Preserve line breaks
        return full_text.strip()
    else:
        return "No response from model."
