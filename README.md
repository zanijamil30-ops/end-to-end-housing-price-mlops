# MLOps Project

An end-to-end **MLOps** pipeline for data preprocessing, model training, evaluation, and deployment using **FastAPI**, **DVC**, **MLflow**, **Docker**, and **AWS** services.

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

### Install Dependencies
```
pip install -r requirements.txt
Build & Run Docker

make build
docker run -p 8000:8000 mlops_project
Run Locally

make serve
CI/CD Pipeline
CI: Linting, testing, and DVC checks via GitHub Actions.

CD: Deploys app to AWS EC2 on main branch updates.

Testing

make test
Contributing
Fork the repo

Create a new branch

Make your changes and create a PR

License
MIT License - See LICENSE

Contact
Your Name: ZAINAB JAMIL
Email: zanijamil30@gmail.com
