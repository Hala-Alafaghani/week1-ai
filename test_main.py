import pytest
from main import load_questions_from_json, Question

def test_question_model_creation():
    q = Question(text="ما هو المتوسط الحسابي للأعداد 2, 4, 6, 8؟", language="ar", reference_answer="5")
    assert q.text == "ما هو المتوسط الحسابي للأعداد 2, 4, 6, 8؟"
    assert q.language == "ar"
    assert q.reference_answer == "5"

def test_load_returns_list():
    questions = load_questions_from_json("questions.json")
    assert isinstance(questions, list)

def test_load_questions_creates_question_instances():
    questions = load_questions_from_json("questions.json")
    assert len(questions) > 0
    assert isinstance(questions[0], Question)