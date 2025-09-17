from fastapi import APIRouter
from app.routes import metrics  # Use this name consistently

router = APIRouter()
feedback_storage = []

@router.post("/")
def submit_feedback(data: dict):
    """
    Expected JSON:
    {
        "text": "I hate this product",
        "predicted": "toxic",
        "correct": "safe"
    }
    """
    # Store feedback
    feedback_storage.append(data)

    # Update feedback metrics
    predicted = data.get("predicted")
    correct = data.get("correct")
    metrics.update_feedback_metrics(predicted, correct)

    return {
        "status": "received",
        "data": data
    }
