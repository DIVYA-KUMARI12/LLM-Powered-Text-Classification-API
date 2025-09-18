import requests
import json
import time
import numpy as np 

BASE_URL = "http://127.0.0.1:8000"

resp = requests.get(f"{BASE_URL}/healthz")
print("Health check:", resp.json())

texts = [
    "I hate this product",
    "Win money now!",
    "I love this app"
]

latencies = []

for text in texts:
    start_time = time.time()
    resp = requests.post(f"{BASE_URL}/classify", json={"text": text})
    end_time = time.time()
    latency_ms = (end_time - start_time) * 1000
    latencies.append(latency_ms)

    result = resp.json()
    result["latency_ms"] = round(latency_ms, 2)  # overwrite with measured latency
    print("Classify:", result)

feedbacks = [
    {"text": "I hate this product", "predicted": "toxic", "correct": "safe"},
    {"text": "Win money now!", "predicted": "spam", "correct": "spam"},
    {"text": "I love this app", "predicted": "safe", "correct": "safe"}
]

for fb in feedbacks:
    resp = requests.post(f"{BASE_URL}/feedback", json=fb)
    print("Feedback:", resp.json())

resp = requests.get(f"{BASE_URL}/metrics")
metrics = resp.json()

avg_latency = round(np.mean(latencies), 2)
p95_latency = round(np.percentile(latencies, 95), 2)
metrics["classification"]["average_latency_ms_measured"] = avg_latency
metrics["classification"]["p95_latency_ms"] = p95_latency

print("Metrics:", json.dumps(metrics, indent=2))