from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

def generate_text_with_conversation(messages):
    client = genai.Client(api_key = os.getenv('GOOGLE_API_KEY'))
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages
    )
    return response.text