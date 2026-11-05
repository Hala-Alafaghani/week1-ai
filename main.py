import json
from pydantic import BaseModel

class Question(BaseModel):
    text: str
    language: str
    reference_answer: str

def load_questions_from_json(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [
        Question(
            text=item["question"],
            language="ar",
            reference_answer=item["answer"]
        )
        for item in data
    ]

def build_prompt(question: Question) -> str:
    return f"Answer the following question in {question.language}: {question.text}"

def generate_answer(question: Question) -> str:
    prompt = build_prompt(question)
    return f"Response to: {question.text}"