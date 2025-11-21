from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter("sample_app_requests_total", "Total Request Count", ["endpoint"])
REQUEST_LATENCY = Histogram("sample_app_request_latency_seconds", "Request latency", ["endpoint"])

@app.route("/")
def index():
    REQUEST_COUNT.labels(endpoint="/").inc()
    return jsonify({"message": "Monitoring-enabled Sample App running!"})

@app.route("/health")
def health():
    REQUEST_COUNT.labels(endpoint="/health").inc()
    return jsonify({"status": "healthy"})

@app.route("/slow")
def slow():
    REQUEST_COUNT.labels(endpoint="/slow").inc()
    with REQUEST_LATENCY.labels(endpoint="/slow").time():
        time.sleep(random.uniform(0.2, 1.0))
    return jsonify({"status": "slow endpoint complete"})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
