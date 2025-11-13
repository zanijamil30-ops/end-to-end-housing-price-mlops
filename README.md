# MLOps Project

An end-to-end **MLOps** pipeline for data preprocessing, model training, evaluation, and deployment using **FastAPI**, **DVC**, **MLflow**, **Docker**, and **AWS** services.

![architecture](https://github.com/user-attachments/assets/452f2e31-7e78-4a0c-8fc2-5dfb72f609c8)

## Technologies Used
- **FastAPI** for serving models via API
- **MLflow** for experiment tracking
- **DVC** for data versioning
- **Docker** for containerization
- **AWS EC2** for cloud hosting
- **Prometheus** for monitoring

## Setup

### Prerequisites
- Python 3.8+
- Docker
- AWS CLI
- GitHub account

### 🔧 **Install Dependencies**
```
pip install -r requirements.txt

🐳 Build & Run Docker
make build
docker run -p 8000:8000 mlops_project

🚀 Run Locally
make serve

🔄 CI/CD Pipeline
CI: Linting, testing, and DVC pipeline checks via GitHub Actions
CD: Automatic deployment to AWS EC2 on updates to the main branch

🧪 Run Tests
make test

🤝 Contributing
Fork the repository
Create a new branch
Commit your changes
Open a pull request

📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

Contact
Your Name: ZAINAB JAMIL
Email: zanijamil30@gmail.com
