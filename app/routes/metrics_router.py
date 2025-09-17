from fastapi import APIRouter
from app.routes import metrics  # import your metrics.py module

router = APIRouter()

@router.get("/")
def get_metrics():
    """
    Returns the current classification and feedback metrics.
    """
    return {
        "classification": metrics.get_classification_metrics(),
        "feedback": metrics.get_feedback_metrics()
    }
