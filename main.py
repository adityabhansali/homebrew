from Models.gemini_ai import generate_text_with_conversation
from functions import *
from template import react_system_prompt

def coffee_suggester_main():
    prompt = input("Don't know which coffee to drink? Let me know how you're feeling:\n")

    messages = [
        {"role": "model", "parts": [{"text": react_system_prompt}]},
        {"role": "user", "parts": [{"text": prompt}]}
    ]

    initial_response = generate_text_with_conversation(messages)
    initial_json = extract_json_from_text(initial_response)
    if initial_json.get("function_name") == "get_coffee_recepies":
        mood = initial_json["function_parms"]["mood"]
        coffee = get_coffee_recepies(mood)

        messages.append({"role": "model", "parts": [{"text": initial_response}]})
        messages.append({
            "role": "user",
            "parts": [{"text": f"**Action_Response**: {coffee}"}]
        })

        final_response = generate_text_with_conversation(messages)
        print(clean_answer_text(final_response))

    else:
        print("Couldn't interpret mood. Try again!")

if __name__ == "__main__":
    coffee_suggester_main()
