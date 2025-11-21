# DevOps Assessment – Project Repository

This repository contains all 7 DevOps tasks completed as part of the **OneData Software Solutions DevOps Evaluation**.  
Each task is implemented **locally**, covering CI/CD, Kubernetes, GitOps, Automation, Monitoring, and RCA.

---

## 📂 Project List

### **1️⃣ CI/CD Pipeline with Jenkins + Docker**
A local Jenkins pipeline that:
- Pulls source code from GitHub  
- Installs dependencies  
- Runs basic tests  
- Builds & runs a Docker image  
- Sends build result email notifications  
📁 *Directory:* `Jenkins-Docker-Kubernetes_kind/`

---

### **2️⃣ Kubernetes Deployment (Minikube / kind)**
A Dockerized Python app deployed to a local Kubernetes cluster with:
- Deployment  
- Service  
- Optional Ingress for domain routing  
📁 *Directory:* `Jenkins-Docker-Kubernetes_kind/`

---

### **3️⃣ GitOps with Argo CD**
Argo CD monitors a GitOps repo and automatically syncs Kubernetes manifests on changes.  
📁 *Directory:* `devops-app-gitops/`

---

### **4️⃣ End-to-End CI/CD – GitHub Actions → Docker Hub → K8s**
GitHub Actions workflow that:
- Builds and tests the app  
- Builds and pushes Docker images  
- Updates GitOps manifests  
- Triggers auto-deployment via Argo CD  
📁 *Directory:* `devops-app-gitops/`

---

### **5️⃣ Infrastructure Automation – Shell Script + Docker Compose**
Automated setup including:
- Jenkins  
- Redis  
- Nginx reverse proxy  
- Python App (Port: 6000)  
All launched using `setup.sh`.  
📁 *Directory:* `infra-automation/`

---

### **6️⃣ Monitoring Stack – Prometheus + Grafana**
Prometheus scrapes custom `/metrics` endpoint from a Flask app, visualized using Grafana dashboards.  
📁 *Directory:* `Monitoring/`

---

### **7️⃣ Simulated Production Incident & RCA**
A buggy app producing random failures.  
Includes:
- Log capture  
- Issue reproduction  
- Root cause analysis  
- Proposed fix  
📁 *Directory:* `incident-debug/`

---

## 📸 Screenshots & Video Evidence

### 🎥 **Project Walkthrough Video**
`https://vimeo.com/1139226781?fl=tl&fe=ec`

### 📷 **Screenshots**

Screenshots for the Above task `https://docs.google.com/document/d/1yTBdq-oj6YG6ZJowFMqMvarF4RC9xX1v1uF34GjurVI/edit?usp=sharing` 

---

## 🧰 Technologies Used

- Git, GitHub  
- Jenkins, GitHub Actions  
- Docker, Docker Compose  
- Kubernetes (Minikube / kind)  
- Argo CD  
- Prometheus, Grafana  
- Python, Bash  
- Nginx, Redis  

---

## 🧑‍💻 About Me

I’m **Gokul K**, a DevOps Engineer Fresher passionate about automation, cloud systems, CI/CD pipelines, containerization, and real-world problem solving.

---

## 🤝 Connect With Me

🔗 LinkedIn: `https://www.linkedin.com/in/gokul-k30/`  
💻 GitHub: https://github.com/Gokulk-306  
📧 Email: **ceecgokul2024@gmail.com**

---

