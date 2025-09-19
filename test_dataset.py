import json
import requests

API_URL = "http://127.0.0.1:8000/classify/"

# Load dataset
with open("eval/dataset.jsonl", "r") as f:
    dataset = [json.loads(line) for line in f]

# Send each text to API
for item in dataset:
    payload = {"text": item["text"]}
    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        print(f"Text: {item['text']}")
        print(f"True Label: {item.get('label')}")
        print(f"Predicted: {result['class']}, Confidence: {result['confidence']}")
        print("-" * 50)
    else:
        print(f"Error {response.status_code} for text: {item['text']}")