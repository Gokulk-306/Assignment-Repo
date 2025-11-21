# GitOps Workflow with Argo CD – Local Environment

This task implements a complete **GitOps-style deployment workflow** using **Argo CD** and **Kubernetes (kind cluster)** running entirely on the local machine.

The workflow automatically deploys Kubernetes manifests whenever changes are pushed to the GitOps repository.

---

## 🎯 Objective

- Deploy Argo CD locally  
- Store Kubernetes manifests in a dedicated GitOps repository  
- Configure Argo CD to watch the repo  
- Any commit → auto-sync → app redeployed  
- Validate automatic version updates using GitHub Actions

---

## What Was Implemented

### ✅ 1. Created a Separate GitOps Repository  
- Repo: **devops-app-gitops**
- Contains only Kubernetes manifests:
  - `deployment.yaml`
  - `service.yaml`
  - `ingress.yaml`
  - `argocd-app.yaml`

This ensures clean separation between **App Repo** and **GitOps Repo**.

---

## 🏗️ 2. Installed Argo CD on Local Cluster

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Exposed the UI:

```bash
kubectl port-forward svc/argocd-server -n argocd 8090:443
```

Argo CD UI available at:  
👉 https://localhost:8090

---

## 🔑 3. Configured Argo CD Login

```bash
argocd login localhost:8090 --username admin --password <initial-password> --insecure
```

Password fetched using:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret   -o jsonpath="{.data.password}" | base64 -d
```

---

## 📦 4. Added the GitOps App to Argo CD

Applied:

```bash
kubectl apply -f argocd-app.yaml
```

Argo CD now watches this repo:

```
https://github.com/Gokulk-306/devops-app-gitops
```

---

## 🔄 5. Automatic Sync Verified

When updating image version using GitHub Actions CI/CD pipeline:

- GitHub Actions updates the `deployment.yaml` image tag  
- Commit pushed to GitOps repo  
- Argo CD detects changes  
- Syncs and redeploys automatically  
- New pod with updated image starts running  

✔ Verified via:

```bash
kubectl get pods
kubectl describe deployment devops-app
```

---

## 🧪 6. Validation of Automatic Deployment

Changed image tag:

```
image: gokulk306/devops-python-app:vX
```

GitHub Actions updated it programmatically using:

```bash
sed -i "s|image: .*|image: gokulk306/devops-python-app:${{ env.IMAGE_TAG }}|" k8s/deployment.yaml
```

Argo CD instantly redeployed the new version.

**Result:**  
🚀 Full GitOps pipeline works end‑to‑end.

---

## ✔️ Task Status: Completed

This README explains exactly what was built:

- Argo CD setup  
- GitOps repo structure  
- Automated sync  
- CI → GitOps → Cluster deployment  
- Successful image updates and redeployments  

All requirements fully satisfied.