# Infrastructure Automation – DevOps Assessment (Local Setup)

This project implements a **fully automated local DevOps infrastructure** using:

- **Docker Compose**
- **Shell automation script (setup.sh)**
- **Nginx reverse proxy**
- **Python Flask application**
- **Redis**
- **Jenkins**

All components run **locally**, without any cloud services, exactly as required in the assignment.

---

## 🏗️ Architecture Overview

This infrastructure contains **four integrated services**:

| Service        | Description |
|----------------|-------------|
| **Jenkins**    | Local CI server running in Docker |
| **Redis**      | In-memory store for application use |
| **Sample Flask App** | Python API app running on **port 6000** |
| **Nginx**      | Reverse proxy routing traffic to the Flask app |

All services are orchestrated with **docker-compose**, and the entire environment is prepared automatically using **setup.sh**.

---

## 📁 Project Structure

```
infra-automation/
├── docker-compose.yml
├── setup.sh
├── sample-app/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── nginx/
    └── nginx.conf
```

---

# ⚙️ How to Run the Entire Infrastructure

### 1️⃣ Make the script executable

```bash
chmod +x setup.sh
```

### 2️⃣ Execute the automation script

```bash
./setup.sh
```

The script automatically:

✔ Installs Docker (if missing)  
✔ Installs docker-compose (if missing)  
✔ Builds the sample app image  
✔ Starts all containers  
✔ Performs health checks  
✔ Shows logs and Jenkins admin password  

---

# 🔍 Health Check Endpoints

### ✔ Flask App (direct)
```
http://localhost:6000/health
```

### ✔ Nginx Reverse Proxy
```
http://localhost:8082/
http://localhost:8082/health
```

### ✔ Redis
```
docker exec redis redis-cli ping
```
**Expected output:**
```
PONG
```

### ✔ Jenkins
```
http://localhost:8080
```

To retrieve Jenkins admin password:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

---

# 🐳 Docker Compose Services

### Jenkins
Runs on:
```
localhost:8080
```

### Redis
Persistent storage enabled at:
```
localhost:6379
```

### Sample App
Python Flask app running on:
```
localhost:6000
```

### Nginx Reverse Proxy
Accessible at:
```
localhost:8082
```

---

# 📌 Key Configurations

### ✔ Flask app runs on **port 6000**
Defined in:
```
app.py
Dockerfile
docker-compose.yml
nginx.conf
```

### ✔ Nginx listens on **port 8082**
Configured in:
```
docker-compose.yml
nginx/nginx.conf
```

### ✔ Redis persistency enabled
Configured with append-only mode.

### ✔ Jenkins runs fully inside Docker

---

# 🧪 Verified Outputs (Your Test Results)

You successfully validated:

```
curl http://localhost:6000/health
→ {"status":"healthy"}

curl http://localhost:8082
→ {"message":"Sample App running behind Nginx & Docker Compose!"}

docker exec redis redis-cli ping
→ PONG

curl -I http://localhost:8080
→ 403 Forbidden (expected for Jenkins before login)
```

Everything is functioning exactly as expected.

---

# 🎯 Task 5 — Status: **COMPLETED**

This README covers **exactly what you implemented**:

✔ Docker Compose automation  
✔ Redis setup  
✔ Flask app (port 6000)  
✔ Nginx reverse proxy (port 8082)  
✔ Jenkins in Docker  
✔ Full automation via setup.sh  
✔ Health checks  
✔ Validation commands  

---
