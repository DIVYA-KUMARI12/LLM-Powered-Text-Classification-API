# app/routes/metrics.py

classification_metrics = {
    "total_requests": 0,
    "class_distribution": {
        "toxic": 0,
        "spam": 0,
        "safe": 0
    },
    "latencies": []
}

feedback_metrics = {
    "total_feedback": 0,
    "correct_count": 0,
    "incorrect_count": 0
}

def update_classification_metrics(classification: str, latency_ms: float):
    classification_metrics["total_requests"] += 1
    if classification in classification_metrics["class_distribution"]:
        classification_metrics["class_distribution"][classification] += 1
    classification_metrics["latencies"].append(latency_ms)

def update_feedback_metrics(predicted: str, correct: str):
    feedback_metrics["total_feedback"] += 1
    if predicted == correct:
        feedback_metrics["correct_count"] += 1
    else:
        feedback_metrics["incorrect_count"] += 1

def get_classification_metrics():
    avg_latency = (
        sum(classification_metrics["latencies"]) / len(classification_metrics["latencies"])
        if classification_metrics["latencies"] else 0
    )
    return {
        "total_requests": classification_metrics["total_requests"],
        "class_distribution": classification_metrics["class_distribution"],
        "average_latency_ms": avg_latency
    }

def get_feedback_metrics():
    return feedback_metrics
