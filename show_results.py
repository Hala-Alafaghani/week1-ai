import json

with open('comparison_results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("--- AI Tutor Model Evaluation Results ---")
for r in data[:5]:
    print(f"Question ID: {r['id']}")
    print(f"Latency: {r['latency_sec']} seconds | Tokens: {r['tokens']}")
    print(f"Answer: {r['qwen_response'][:100]}...")
    print("-" * 40)