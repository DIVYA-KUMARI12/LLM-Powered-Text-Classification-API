import json
import requests
import time
from collections import defaultdict
import numpy as np  # For percentile calculation

# Base URL for your running FastAPI classification API
BASE_URL = "http://127.0.0.1:8000/classify"

# Load evaluation dataset
dataset_file = "eval/dataset.jsonl"
dataset = []
with open(dataset_file, "r") as f:
    for line in f:
        dataset.append(json.loads(line.strip()))

# Lists to store true labels, predicted labels, and request latencies
true_labels = []
pred_labels = []
latencies = []

# Loop through dataset and call /classify for each example
for item in dataset:
    true_labels.append(item["label"])  # store actual label

    # Measure the time taken for each API request
    start_time = time.time()
    response = requests.post(BASE_URL, json={"text": item["text"]})
    end_time = time.time()
    latency_ms = (end_time - start_time) * 1000
    latencies.append(latency_ms)

    # Store predicted class; fallback to "safe" if API fails
    if response.status_code == 200:
        pred = response.json().get("class")
        pred_labels.append(pred)
    else:
        print(f"Error calling API for text: {item['text']}")
        pred_labels.append("safe")

# Initialize metrics storage for each class
classes = ["toxic", "spam", "safe"]
metrics = defaultdict(lambda: {"TP": 0, "FP": 0, "FN": 0})

# Count True Positives, False Positives, False Negatives for each class
for true, pred in zip(true_labels, pred_labels):
    for cls in classes:
        if pred == cls and true == cls:
            metrics[cls]["TP"] += 1
        if pred == cls and true != cls:
            metrics[cls]["FP"] += 1
        if pred != cls and true == cls:
            metrics[cls]["FN"] += 1

# Compute precision, recall, and F1 score per class
results = {}
for cls in classes:
    tp = metrics[cls]["TP"]
    fp = metrics[cls]["FP"]
    fn = metrics[cls]["FN"]

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    # Round metrics to 2 decimal places for readability
    results[cls] = {"precision": round(precision, 2),
                    "recall": round(recall, 2),
                    "f1": round(f1, 2)}

# Calculate overall accuracy
accuracy = sum(1 for t, p in zip(true_labels, pred_labels) if t == p) / len(true_labels)

# Compute average latency and 95th percentile latency
avg_latency = round(np.mean(latencies), 2)
p95_latency = round(np.percentile(latencies, 95), 2)

# Print all evaluation results
print("===== Evaluation Results =====")
print(f"Overall Accuracy: {accuracy:.2f}\n")
for cls, m in results.items():
    print(f"{cls.capitalize()} -> Precision: {m['precision']}, Recall: {m['recall']}, F1: {m['f1']}")
print(f"\nAverage Latency (ms): {avg_latency}")
print(f"95th Percentile Latency (ms): {p95_latency}")