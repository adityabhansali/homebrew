import gradio as gr
from Models.gemini_ai import generate_text_with_conversation
from functions import *
from template import react_system_prompt

def suggest_coffee(mood_input):
    messages = [
        {"role": "model", "parts": [{"text": react_system_prompt}]},
        {"role": "user", "parts": [{"text": mood_input}]}
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
        return clean_answer_text(final_response)
    else:
        return "Couldn't interpret your mood. Try describing it differently!"

# Gradio Interface
iface = gr.Interface(
    fn=suggest_coffee,
    inputs=gr.Textbox(lines=2, placeholder="How are you feeling today?"),
    outputs=gr.Textbox(label="Suggested Coffee"),
    title="Coffee Suggestor ☕",
    description="Tell me your mood, and I'll suggest the perfect coffee for you!"
)

if __name__ == "__main__":
    iface.launch()
