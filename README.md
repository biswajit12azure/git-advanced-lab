# 🚀 Git Advanced Lab – Python CI/CD & DevSecOps

This repository demonstrates an **end-to-end CI/CD and DevSecOps pipeline** for a **Python application** using **GitHub Actions**, integrated with **code quality checks, security scanning**, and **Kubernetes deployment manifests**.

It is designed as a **hands-on lab** to understand **advanced Git workflows, CI/CD automation, and DevSecOps best practices**.

---

## 📌 Repository Objectives

- Implement CI/CD for a Python application  
- Practice advanced Git operations  
- Integrate DevSecOps tools (SonarQube, CodeQL)  
- Apply containerization and Kubernetes deployment  
- Demonstrate **shift-left security** in pipelines  

---

## 🧱 Project Structure

```text
git-advanced-lab/
│
├── app/                      # Python application source code
│   ├── app.py
│   └── requirements.txt
│
├── tests/                    # Unit test cases
│
├── .github/
│   └── workflows/
│       ├── ci.yml            # CI pipeline (build, test, scan)
│       ├── codeql.yml        # CodeQL security analysis
│       └── sonar.yml         # SonarQube scan
│
├── k8s/                      # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
├── Dockerfile                # Containerization
├── sonar-project.properties  # SonarQube configuration
├── .gitignore
└── README.md


🤝 Contributing

Contributions are welcome!
Feel free to fork this repository, raise issues, or submit pull requests.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author
Maintained by:
Biswajit Dash
DevOps / Cloud / DevSecOps Engineer
CI/CD | Kubernetes | Security Automation
