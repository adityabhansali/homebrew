from template import react_system_prompt
from Models.gemini_ai import generate_text_with_conversation

prompt = "I am feeling lovely! which coffee is best for me to drink?"

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
print(response)