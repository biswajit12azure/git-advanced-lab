# 🚀 Git Advanced Lab – Python CI/CD & DevSecOps

This repository demonstrates an **end-to-end CI/CD and DevSecOps pipeline** for a **Python application** using **GitHub Actions**, with integrated **security scanning (Bandit & CodeQL)**, **Docker containerization**, and **Kubernetes deployment manifests**.

It is designed as a **hands-on lab** to understand **advanced Git workflows, CI/CD automation, and DevSecOps best practices**.

---

## 📌 Repository Objectives

- Implement CI/CD for a Python application using GitHub Actions  
- Practice advanced Git operations  
- Integrate DevSecOps tools (Bandit, CodeQL)  
- Apply Docker-based containerization  
- Deploy applications using Kubernetes manifests  
- Demonstrate **shift-left security** in CI pipelines  

---

## 🧱 Project Structure

```text
git-advanced-lab/
│
├── .github/
│   └── workflows/
│       ├── CI.yml              # Main CI pipeline
│       └── bandit/             # Bandit security scan config/artifacts
│
├── kubernetes/                 # Kubernetes deployment manifests
│
├── tests/                      # Unit test cases
│
├── app.py                      # Python application entry point
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker image definition
└── README.md                   # Project documentation

