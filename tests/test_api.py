import requests

BASE_URL = "http://127.0.0.1:8000"

def test_health():
    print("Testing /healthz endpoint...")
    response = requests.get(f"{BASE_URL}/healthz")
    print("Response:", response.json(), "\n")

def test_classify():
    print("Testing /classify endpoint...")
    data = {"text": "I hate this product"}
    response = requests.post(f"{BASE_URL}/classify/", json=data)
    print("Request:", data)
    print("Response:", response.json(), "\n")

def test_feedback():
    print("Testing /feedback endpoint...")
    data = {
        "text": "I hate this product",
        "predicted": "toxic",
        "correct": "safe"
    }
    response = requests.post(f"{BASE_URL}/feedback/", json=data)
    print("Request:", data)
    print("Response:", response.json(), "\n")

def test_metrics():
    print("Testing /metrics endpoint...")
    response = requests.get(f"{BASE_URL}/metrics/")
    print("Response:", response.json(), "\n")

if __name__ == "__main__":
    test_health()
    test_classify()
    test_feedback()
    test_metrics()