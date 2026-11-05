import json
from llm_client import get_structured_quiz

all_questions = []

print("Generating questions...")
for i in range(20):
    prompt = (
        "Generate a multiple-choice statistics question about Mean, Median, and Mode "
        "in English. Return it strictly as a JSON object with keys: "
        "'question' (str), 'options' (list of 4 strings), and 'correct_answer' (str)."
    )
    quiz_obj = get_structured_quiz(prompt)
    all_questions.append(quiz_obj.model_dump())

with open('questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=4)

print("Successfully generated and saved 20 questions to questions.json!")