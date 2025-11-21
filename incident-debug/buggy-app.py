from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route("/")
def home():
    # Random delay (simulates performance issue)
    delay = random.choice([0, 0.5, 1.5])
    time.sleep(delay)

    # Random crash
    if random.random() < 0.30:  # 30% failure
        raise Exception("Random Failure: Simulated production bug")

    return jsonify({
        "message": "App running (but buggy)",
        "delay": delay
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
