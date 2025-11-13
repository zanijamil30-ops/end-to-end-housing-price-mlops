# Step-by-Step Demo to Run Locally

This guide will walk you through the steps to run the MLOps project locally, from setting up the environment to training the model and serving it via FastAPI.

## Prerequisites

1. **Python**: Version 3.8 or higher
2. **Docker**: For containerizing the FastAPI app and model
3. **Git**: For version control
4. **DVC**: For managing data and model versioning
5. **FastAPI**: For serving the model via an API

Make sure you have the following tools installed:
- [Python](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [DVC](https://dvc.org/doc/install)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

---

## 1. Clone the Repository

First, clone the repository to your local machine:

```
git clone https://github.com/yourusername/your-repository.git
cd your-repository
2. Set Up the Python Environment
Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required Python dependencies:

pip install -r requirements.txt
You will need DVC for managing data and models:

pip install dvc
3. Install Docker (for Containerization)
If you don’t already have Docker installed, you can follow the official instructions to install Docker:

Docker Installation Guide

4. Run the DVC Pipeline
The DVC pipeline ensures that all the steps in the data processing and model training pipeline are executed. You can trigger the pipeline using the following command:

./scripts/run_local.sh
This script will:

Run dvc repro to run the entire pipeline, from fetching the raw data to preprocessing and training the model.

After successful execution, it will start a FastAPI server locally.

The model will be served at http://localhost:8000.

5. Access the FastAPI Server
Once the server is running, you can access the model prediction endpoint.

Example Request Using curl

curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature1": 2000,
  "feature2": 3,
  "feature3": 1
}'
This will return a prediction from the model.

Example Response

{
  "prediction": 350000
}
6. Run Unit and Integration Tests
To ensure everything is working as expected, you can run the unit and integration tests:

pytest
This will execute all tests in the tests/ directory and ensure that all functionality (including preprocessing, prediction, and API) works correctly.

7. Stop the FastAPI Server
To stop the FastAPI server, press CTRL+C in the terminal where the server is running.

8. (Optional) Build and Deploy Docker Image
If you want to containerize the application using Docker, you can build the Docker image using the following script:

./scripts/build_image.sh
This will build a Docker image for the application. Once the image is built, you can deploy it to a cloud provider (e.g., AWS EC2) using the deploy_to_ec2.sh script.

./scripts/deploy_to_ec2.sh
Make sure you have an EC2 instance ready and your SSH keys configured before running the deployment script.
