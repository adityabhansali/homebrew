import json
import re

def extract_json_from_text(text):
    match = re.search(r"\*\*Action\*\*:\s*(\{.*?\})\s*\*\*PAUSE\*\*", text, re.DOTALL)
    if match:
        json_str = match.group(1)
        try:
            data = json.loads(json_str)
            return data
        except json.JSONDecodeError as e:
            print("Failed to parse JSON:", e)
            return None
    else:
        print("No valid JSON block found.")
        return None