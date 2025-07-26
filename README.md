Coffee Recommendation Script
==========================

Overview
--------
This Python script uses a generative AI model to recommend a coffee based on the user's mood. The script leverages a `react_system_prompt` and the `generate_text_with_conversation` function from the `gemini_ai` model to process a user prompt and generate a response.

Prerequisites
-------------
- Python 3.x
- Required libraries:
  - `template` (for accessing `react_system_prompt`)
  - `Models.gemini_ai` (custom module for the `generate_text_with_conversation` function)

Installation
------------
1. Ensure Python 3.x is installed on your system.
2. Install the required dependencies (if applicable):
   ```
   pip install template gemini-ai
   ```
   Note: The `gemini_ai` module is assumed to be a custom or proprietary module. Replace it with the appropriate package or ensure it is available in your project.

3. Verify that the `template` module with `react_system_prompt` is accessible in your project.

Usage
-----
1. Save the script as `coffee_recommendation.py` (or any preferred name).
2. Run the script using:
   ```
   python coffee_recommendation.py
   ```

3. The script will:
   - Import the necessary modules.
   - Define a user prompt ("I am feeling lovely! which coffee is best for me to drink?").
   - Create a message structure combining the `react_system_prompt` and user prompt.
   - Call the `generate_text_with_conversation` function to get a coffee recommendation.
   - Print the response.

Example Output
--------------
The output will depend on the AI model's response. An example might look like:
```
Based on your lovely mood, a light and floral Ethiopian Yirgacheffe coffee would be perfect for you!
```

File Structure
--------------
```
project_directory/
├── coffee_recommendation.py  # Main script
├── template.py              # Module containing react_system_prompt (assumed)
├── Models/
│   └── gemini_ai.py         # Module containing generate_text_with_conversation (assumed)
└── README.md               # This file
```

Notes
-----
- The `react_system_prompt` and `generate_text_with_conversation` are assumed to be pre-defined. Ensure these are correctly implemented and accessible.
- Modify the `prompt` variable in the script to change the user input or mood.
- If `gemini_ai` is a third-party or custom module, refer to its documentation for additional setup or configuration.

License
-------
This project is unlicensed. Use it at your own discretion.