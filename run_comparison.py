import json
import time
import urllib.request

# 1. Load the 20 statistics questions
with open('questions.json', 'r', encoding='utf-8') as f:
    questions_data = json.load(f)

# Handle different JSON structures (list or dict with 'questions' key)
if isinstance(questions_data, dict) and 'questions' in questions_data:
    questions = questions_data['questions']
else:
    questions = questions_data

print(f"Loaded {len(questions)} questions.")

results = []

# 2. Evaluate using local Ollama (qwen2.5:7b)
for idx, q in enumerate(questions, 1):
    q_text = q.get('question', q) if isinstance(q, dict) else str(q)
    
    prompt = f"You are an AI Tutor. Answer the following statistics question concisely in English:\n{q_text}"
    
    payload = json.dumps({
        "model": "qwen2.5:7b",
        "prompt": prompt,
        "stream": False
    }).encode('utf-8')
    
    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    
    start_time = time.time()
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            latency = round(time.time() - start_time, 2)
            answer = res.get('response', '')
            eval_count = res.get('eval_count', 0)
    except Exception as e:
        latency = 0
        answer = f"Error: {e}"
        eval_count = 0
        
    print(f"[{idx}/{len(questions)}] Processed in {latency}s")
    
    results.append({
        "id": idx,
        "question": q_text,
        "qwen_response": answer,
        "tokens": eval_count,
        "latency_sec": latency
    })

# 3. Save evaluation results
with open('comparison_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("\nEvaluation complete! Results saved to comparison_results.json")