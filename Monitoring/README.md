# Monitoring Stack – Prometheus & Grafana (Local Setup)

This project implements a **complete local monitoring system** using:

- **Docker Compose**
- **Python Flask sample app with /metrics endpoint**
- **Prometheus** for metrics scraping
- **Grafana** for metrics visualization

All components run **locally**, without using any cloud services.

---

## 🏗️ Monitoring Architecture Overview

This monitoring environment includes **three main services**:

| Service       | Description |
|---------------|-------------|
| **Sample App** | Python Flask API exposing Prometheus metrics on **port 7000** |
| **Prometheus** | Scrapes `/metrics` from the sample app on **port 9090** |
| **Grafana**    | Visualizes metrics and dashboards on **port 3000** |

All services are orchestrated using **docker-compose**.

---

## 📁 Project Structure

```
Monitoring/
├── docker-compose.yml
├── prometheus/
│   └── prometheus.yml
├── sample-app/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── dashboard.json
```

---

# ⚙️ How to Run the Monitoring Stack

### 1️⃣ Start all services

```bash
docker-compose up -d
```

### 2️⃣ Verify running containers

```bash
docker ps
```

You should see:

- monitoring-sample-app  
- prometheus  
- grafana  

---

# 🔍 Access Endpoints

### ✔ Sample App Metrics  
```
http://localhost:7000/metrics
```

### ✔ Prometheus UI  
```
http://localhost:9090
```

### ✔ Grafana UI  
```
http://localhost:3000
```

### Grafana Login  
```
Username: admin
Password: admin
```

---

# 📌 Setup Prometheus Data Source in Grafana

1. Open Grafana  
2. Go to **Settings → Data Sources**  
3. Add new data source → **Prometheus**  
4. Set URL:

```
http://prometheus:9090
```

5. Click **Save & Test**

---

# 📊 Dashboard

A custom Grafana dashboard was created and exported as:

```
dashboard.json
```

You can import it through:

Grafana → **Dashboards → Import → Upload JSON**

---

# 🛑 Stop All Services

```bash
docker-compose down -v
```

---

# 🎯 Task 6 — Status: COMPLETED

This monitoring setup includes:

✔ Prometheus  
✔ Grafana  
✔ Sample metrics app  
✔ Docker Compose  
✔ Exported dashboard  
✔ Local-only monitoring stack  
