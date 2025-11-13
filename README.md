# end-to-end-housing-price-mlops

This is an end-to-end **MLOps** pipeline that demonstrates the full lifecycle of a machine learning project, from data preprocessing, model training, and evaluation to deployment using **FastAPI**, **DVC**, **MLflow**, **Docker**, and **AWS** services. This project showcases how to build, manage, and deploy a machine learning model using modern MLOps practices.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [How to Run Locally](#how-to-run-locally)
5. [CI/CD Pipeline](#cicd-pipeline)
6. [Testing](#testing)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

## Project Overview

This project automates the machine learning workflow, including:
- **Data Versioning** with **DVC** for handling large datasets.
- **Experiment Tracking** with **MLflow** to log models and hyperparameters.
- **Model Serving** using **FastAPI** for creating a REST API that serves predictions.
- **Dockerization** to ensure portability across different environments.
- **Continuous Integration/Continuous Deployment (CI/CD)** using **GitHub Actions** for automated testing and deployment.

The pipeline includes steps for preprocessing data, training models, logging experiments, and serving the model in a production environment.

## Technologies Used

- **FastAPI**: Web framework for serving the model as an API.
- **MLflow**: For experiment tracking, model management, and deployment.
- **DVC**: Data version control for managing datasets and models.
- **Docker**: Containerization of the application and model for deployment.
- **AWS EC2**: Cloud hosting for the model server.
- **GitHub Actions**: Automates CI/CD pipeline for testing and deployment.
- **Prometheus**: For monitoring metrics related to model serving.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Docker (for containerization)
- AWS CLI (for deployment)
- GitHub account (for version control and CI/CD)

### Installing Dependencies
1. Clone the repository:

   ```
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

pip install -r requirements.txt
Initialize DVC and pull the datasets:

make dvc-init
Docker Setup
Build the Docker image for the FastAPI app:

make build
Run the Docker container locally:

docker run -p 8000:8000 $(DOCKER_IMAGE_NAME)
How to Run Locally
Start FastAPI server:

After setting up the environment, you can run the FastAPI app locally:
make serve
Test the API:

You can send requests to the FastAPI server running locally at http://localhost:8000. Use the following command to test the /predict endpoint:

curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature1": 2000,
  "feature2": 3,
  "feature3": 1
}'
Run DVC pipeline:

You can run the entire data processing and model training pipeline with DVC:

make dvc-repro
CI/CD Pipeline
The CI/CD pipeline for this project is configured using GitHub Actions. The pipeline includes:

Continuous Integration (CI): Linting, running tests, and ensuring that the code quality is maintained.

Continuous Deployment (CD): Deploys the application to an AWS EC2 instance when changes are merged into the main branch.

GitHub Actions Workflow
The workflows are defined in .github/workflows/ and include:

ci.yml: For linting, testing, and DVC pipeline checks.

cd.yml: For deploying the application to AWS.

Testing
This project includes both unit tests and integration tests for all major components. To run the tests:

make test
The tests are defined in the tests/ directory and include tests for:

Preprocessing scripts

Prediction logic

API endpoints

Contributing
We welcome contributions to this project! To contribute:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m "Add a new feature").

Push to your fork (git push origin feature/your-feature-name).

Create a pull request with a detailed description of your changes.

Please follow the guidelines in the CONTRIBUTING.md file when submitting a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any questions or feedback, feel free to reach out to:

Your Name: ZAINAB JAMIL

Email: zanijamil30@gmailcom

Thank you for using this MLOps project! Happy coding!

