# 🚨 Simulated Production Incident – Root Cause Analysis (RCA)

This task simulates a real-world production issue where a Python Flask application behaves inconsistently, returning random 500 errors. Below is the full RCA based on the investigation, reproduction, log capture, and proposed fix.

---

## 📌 Incident Summary

A Dockerized Python Flask application was deployed locally on **port 5001**.  
During repeated access, the root endpoint (`/`) showed:

- **Intermittent HTTP 200 OK**
- **Intermittent HTTP 500 Internal Server Error**

The `/health` endpoint was always stable.

This indicates the issue was **specific to the main application route**.

---

## 🧪 Steps to Reproduce

### 1️⃣ Build and run the buggy app
\`\`\`bash
docker build -t buggy-app .
docker run -p 5001:5000 buggy-app
\`\`\`

### 2️⃣ Make repeated requests
\`\`\`bash
while true; do curl -I http://localhost:5001/; sleep 1; done
\`\`\`

### 🔍 Observed Behavior

- Random **HTTP 200** and **HTTP 500** responses.
- `/health` always returned:
  \`\`\`json
  {"status": "ok"}
  \`\`\`

---

## 📜 Logs Captured (Actual Output)

\`\`\`
Exception: Random Failure: Simulated production bug
172.17.0.1 - - "HEAD / HTTP/1.1" 500 -
ERROR in app: Exception on / [HEAD]
Traceback (most recent call last):
  ...
  File "/app/buggy-app.py", line 15, in home
      raise Exception("Random Failure: Simulated production bug")
Exception: Random Failure: Simulated production bug
\`\`\`

---

## 🧠 Root Cause

Inside \`buggy-app.py\`, the root endpoint was intentionally designed to fail at random:

\`\`\`python
if random.choice([True, False]):
    raise Exception("Random Failure: Simulated production bug")
\`\`\`

This code produces **50% failure responses**, triggering intermittent 500 errors.

### ✔ Why it Happened?

- The app simulates real-world instability.
- No error handling exists.
- Failure is intentional.

---

## 🩹 Proposed Fix

### ✅ Fix 1 — Remove Random Failure

\`\`\`python
return jsonify({"message": "App is working reliably"})
\`\`\`

### ✅ Fix 2 — Add Error Handling (better option)

\`\`\`python
try:
    if random.choice([True, False]):
        raise Exception("Random Failure: Simulated production bug")
    return jsonify({"status": "ok"})
except Exception as e:
    app.logger.error(f"Error occurred: {e}")
    return jsonify({"error": "Internal error occurred"}), 500
\`\`\`

### ✅ Fix 3 — Add Observability

- Enable Prometheus metrics  
- Add structured logging  
- Add retries or circuit breaker (service mesh or code logic)  

---

## 🧩 Impact Analysis

| Area | Impact |
|------|--------|
| User Experience | Frequent service failures |
| Logs | High volume of error logs |
| Reliability | Degraded service stability |
| Monitoring | Random spikes in error rate |

---

## 🛠️ Preventive Measures

- Add unit tests to validate API stability  
- Add centralized logging (ELK / Loki)  
- Add automated retries  
- Add CI checks for exception handling  
- Implement graceful error-handling in endpoints  

---

## ✅ Final Result

The issue was:

✔ Reproduced  
✔ Debugged  
✔ Logs captured  
✔ Root cause identified  
✔ Fix documented  

This completes **Task 7 — Simulated Production Incident & RCA**.

---
