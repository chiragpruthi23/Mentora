'''
Project: Mentora; Version - 1.0.2
Author: Chirag Pruthi
Tech Used: Groq AI, Python Modules(Groq, OS, Dotenv)
'''

import groq
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key from environment variable
client = groq.Groq(api_key=os.getenv('GROQ_API_KEY'))

# Function to generate unique questions from Groq AI
def generate_question():
    prompt = "Generate a unique multiple-choice question about mental well-being, including stress, sleep, focus, hydration, etc. Provide 4 answer options (a-d)."

    # Using Groq's chat completion API
    response = client.chat.completions.create(
        model="llama3-70b-8192",  # Using LLaMA 3 model (or another available Groq model)
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.7,
    )

    question = response.choices[0].message.content.strip()
    return question

# Function to interpret user answer and suggest a tip
def interpret_answer(user_answer):
    prompt = f"The user selected the answer: '{user_answer}'. Interpret the user's mental state and suggest one biology-based health tip. For example: advice about sleep, hydration, or relaxation."

    # Using Groq's chat completion API for interpretation
    response = client.chat.completions.create(
        model="llama3-70b-8192",  # Using LLaMA 3 model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.7,
    )

    tip = response.choices[0].message.content.strip()
    return tip

# Main function to run the quiz
def mental_fitness_quiz():
    questions_asked = 0
    total_questions = 10  # You can modify this number as needed

    while questions_asked < total_questions:
        print(f"\nQuestion {questions_asked + 1} of {total_questions}:")
        
        # Generate the question dynamically
        question = generate_question()
        print(question)
        
        # Ask user to select an option (simulating an answer selection)
        user_answer = input("Select your answer (a/b/c/d): ").strip().lower()

        if user_answer in ['a', 'b', 'c', 'd']:  # Ensure valid answer
            print(f"\nYou selected: {user_answer.upper()}")

            # Get the AI's interpretation and wellness tip
            tip = interpret_answer(user_answer)
            print(f"\nAI's tip: {tip}\n")

            questions_asked += 1
            time.sleep(1)  # Adding a slight pause between questions
        else:
            print("Invalid answer. Please choose between a, b, c, or d.")

    print("\nThank you for completing the quiz!")

# Run the quiz
if __name__ == "__main__":
    mental_fitness_quiz()
