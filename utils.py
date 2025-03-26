import os
import openai

# Set your OpenAI API key as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def process_question(question, file):
    # Check if question is empty
    if not question.strip():
        return "Please provide a valid question."

    # Prepare the prompt
    prompt = f"Answer the following question concisely:\n{question}"

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response["choices"][0]["message"]["content"]
