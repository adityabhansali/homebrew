from template import react_system_prompt
from Models.gemini_ai import generate_text_with_conversation
from functions import *
prompt = input('Dont know which coffee to drink? Let me know how you feeling? Let me guide you to feel the heaven!')

messages = [
    {
        "role": "model",
        "parts": [{"text": react_system_prompt}]
    },
    {
        "role": "user",
        "parts": [{"text": prompt}]
    }
]

response = generate_text_with_conversation(messages)
response = extract_json_from_text(response)
