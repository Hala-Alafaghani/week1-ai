from main import load_questions_from_json, Question, build_prompt, generate_answer

def test_question_model():
    q = Question(text="Test?", language="en", reference_answer="Yes")
    assert q.language == "en"

def test_load_questions():
    questions = load_questions_from_json("questions.json")
    assert len(questions) > 0
    assert isinstance(questions[0], Question)

def test_question_text():
    questions = load_questions_from_json("questions.json")
    assert questions[0].text is not None

def test_build_prompt():
    q = Question(text="What is Python?", language="en", reference_answer="A language")
    prompt = build_prompt(q)
    assert "What is Python?" in prompt
    assert "en" in prompt

def test_generate_answer():
    q = Question(text="What is Python?", language="en", reference_answer="A language")
    answer = generate_answer(q)
    assert answer is not None
    assert len(answer) > 0
