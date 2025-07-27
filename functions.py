import json
import re
import ast
import os

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

def save_unknown_mood(mood: str, file_path="moods.json"):
    mood = mood.lower()
    
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            existing = json.load(f)
    else:
        existing = []

    if mood not in existing:
        existing.append(mood)
        with open(file_path, "w") as f:
            json.dump(existing, f, indent=4)
        print(f"New mood '{mood}' saved to moods.json")
    else:
        print(f"Mood '{mood}' already exists in moods.json")

def get_coffee_recepies(mood: str) -> str:
    mood = mood.lower()
    match mood:
        case "happy":
            return "Iced Caramel Latte"
        case "sad":
            return "Mocha with extra chocolate"
        case "tired":
            return "Espresso shot"
        case "excited":
            return "Cold Brew with lemon"
        case "lonely":
            return "Coffechino"
        case "angry":
            return "Flat White with oat milk"
        case "anxious":
            return "Decaf Chamomile Latte"
        case "stressed":
            return "Vanilla Lavender Latte"
        case "relaxed":
            return "Hazelnut Flat White"
        case "bored":
            return "Affogato (espresso over ice cream)"
        case "confident":
            return "Macchiato"
        case "romantic":
            return "Rose Latte"
        case "nostalgic":
            return "Turkish Coffee"
        case "playful":
            return "Peppermint Mocha"
        case "focused":
            return "Americano"
        case "creative":
            return "Spanish Latte"
        case "lazy":
            return "Iced Coffee with cream"
        case "determined":
            return "Doppio (double espresso)"
        case "hopeful":
            return "Cinnamon Cappuccino"
        case "curious":
            return "Nitro Cold Brew"
        case _:
            save_unknown_mood(mood)
            return "Classic Cappuccino"


def extract_json_from_text(text):
    try:
        match = re.search(r"{.*}", text, re.DOTALL)
        if match:
            return ast.literal_eval(match.group(0))
    except Exception as e:
        print("Error parsing JSON:", e)
    return {}

def clean_answer_text(response_text):
    answer_match = re.search(r"\*\*Answer\*\*: (.+?)\n", response_text)
    answer = answer_match.group(1).strip() if answer_match else ""

    ingredients = re.findall(r"\*\*Ingredients\*\*:\n(.*?)\n\n", response_text, re.DOTALL)
    ingredients_list = []
    if ingredients:
        ingredients_list = [line.strip('* ').strip() for line in ingredients[0].strip().split('\n') if line.strip()]

    instructions = re.findall(r"\*\*Instructions\*\*:\n(.*?)$", response_text, re.DOTALL)
    instructions_list = []
    if instructions:
        instructions_list = [re.sub(r"^\d+\.\s*", "", line).strip() for line in instructions[0].strip().split('\n') if line.strip()]

    data = {
        "answer": answer,
        "recipe": {
            "ingredients": ingredients_list,
            "instructions": instructions_list
        }
    }
    return json.dumps(data, indent=4)
    