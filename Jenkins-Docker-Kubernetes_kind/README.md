# 🚀 DevOps Assessment – CI/CD Pipeline & Kubernetes Deployment

This document explains the work completed for **Task 1** and **Task 2** of the DevOps Assignment.  
Everything was executed **locally** using Docker, Jenkins, and Kind (Kubernetes in Docker).

---

## ✅ Task 1: CI/CD Pipeline with Jenkins + Docker

For this task, I set up a complete CI/CD pipeline fully running on my local machine.

### ✔ What I implemented

- Installed and ran **Jenkins** locally using Docker.
- Connected **GitHub** to Jenkins using a webhook so every commit automatically triggers a build.
- Jenkins pipeline:
  - Pulled the source code from GitHub  
  - Created a Python virtual environment  
  - Installed dependencies  
  - Performed a basic test (syntax check)  
  - Built a Docker image of the application  
  - Ran the Docker container automatically on successful build  
- Added **email notifications** for both successful and failed builds.

### ✔ Result

Every push to the GitHub repository triggers an automated pipeline in Jenkins, builds the Docker image, and deploys the application locally.

---

## ✅ Task 2: Kubernetes Deployment with Kind (Local Kubernetes)

For the second task, I deployed the same Dockerized application into a **local Kubernetes cluster**.

### ✔ What I implemented

- Created all required Kubernetes manifests:
  - Deployment  
  - Service  
- Used **Kind** as the local Kubernetes environment.
- Loaded the Docker image into the Kind cluster.
- Applied the Kubernetes YAML files using:

  ```bash
  kubectl apply -f k8s/
  ```

- Verified that the pods and services were running successfully.
- Exposed the application using **NodePort**, then accessed it locally using curl.

### ✔ Result

The application is deployed inside a local Kubernetes cluster and is fully accessible through NodePort.  
All pods and services run successfully and can be validated with kubectl commands.

---

## 🎯 Conclusion

Both tasks were successfully completed:

- CI/CD pipeline: **GitHub → Jenkins → Docker → Local Deployment**
- Kubernetes deployment: **Docker image → Kind cluster → Running pods & service**

This completes **Task 1 and Task 2** of the DevOps assignment.
