from fastapi import FastAPI
from app.routes import classify, feedback
from app.routes import metrics_router  

app = FastAPI()

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

app.include_router(classify.router, prefix="/classify", tags=["Classification"])
app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])
app.include_router(metrics_router.router, prefix="/metrics", tags=["Metrics"]) 