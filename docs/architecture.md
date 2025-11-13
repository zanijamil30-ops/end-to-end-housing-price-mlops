# System Architecture

This document describes the architecture of the MLOps pipeline implemented for this project. It includes details about data flow, model training, deployment, and the tools used throughout the process.

## Overview

The architecture of the system can be broken down into several components:

1. **Data Pipeline**
   - The data is first stored as raw data (`housing.csv`) and is processed using `preprocess.py` for cleaning and transformation.
   - The processed data is then used for training the machine learning model.

2. **Model Training**
   - The model is trained using the preprocessed data in the `train.py` script.
   - The training process logs hyperparameters, metrics, and the trained model using **MLflow**, ensuring versioning and experiment tracking.
   
3. **Model Serving**
   - The trained model is served via a **FastAPI** application.
   - FastAPI exposes an endpoint (`/predict`) that allows users to send input data and get predictions from the model.

4. **Model Versioning & Experimentation**
   - **MLflow** is used to track and manage experiments, including hyperparameters, model metrics, and artifacts (e.g., trained model).
   - **DVC (Data Version Control)** is used to version the datasets and track changes in the data and model files, ensuring reproducibility.

5. **Continuous Integration & Deployment (CI/CD)**
   - **GitHub Actions** is used for automating the build, test, and deployment processes. The `ci.yml` file handles continuous integration (e.g., linting, unit tests), while the `cd.yml` file automates the deployment pipeline.
   - The model and API are containerized using **Docker** to ensure consistency across environments and ease of deployment.

6. **Deployment**
   - The model is deployed to **AWS EC2** instances using Docker. The `deploy_to_ec2.sh` script automates the process of building and deploying the Docker image to the EC2 instance.


### Key Components in the Diagram:

1. **Raw Data**:
   - The `housing.csv` file contains the raw data. It is stored in the `data/raw/` directory and used for processing.
   
2. **Data Preprocessing**:
   - The `preprocess.py` script is responsible for transforming raw data into a clean, usable format. This includes handling missing values, feature scaling, and encoding categorical features.

3. **Model Training**:
   - The `train.py` script trains the machine learning model using the preprocessed data. The model is logged and versioned with **MLflow**.

4. **Model Management with MLflow**:
   - MLflow is used to log model metrics, hyperparameters, and artifacts. It also helps in managing the model lifecycle.

5. **FastAPI Model Serving**:
   - FastAPI serves the model as a REST API. The `/predict` endpoint takes input data in JSON format, makes predictions using the trained model, and returns the result.
   
6. **DVC (Data Version Control)**:
   - DVC is used for versioning the dataset and the trained model. The data pipeline (`dvc.yaml`) ensures reproducibility and consistency.

7. **Docker**:
   - The application (training and serving) is containerized using Docker, which ensures that the project can be deployed on any machine, including EC2 instances.

8. **CI/CD with GitHub Actions**:
   - GitHub Actions is used for continuous integration and deployment. The `ci.yml` and `cd.yml` files automate the testing, model training, and deployment process.

9. **Cloud Deployment (AWS EC2)**:
   - The final model is deployed on **AWS EC2** instances using Docker containers. The `deploy_to_ec2.sh` script automates the deployment process.

## Technologies Used

- **DVC**: Data versioning for dataset and model management.
- **MLflow**: Model tracking and experiment management.
- **FastAPI**: Web framework for serving the model via an API.
- **Docker**: Containerization of the application for deployment.
- **GitHub Actions**: CI/CD pipeline automation for testing and deployment.
- **AWS EC2**: Cloud infrastructure for deploying the application.

## Data Flow

1. **Data Preprocessing**: 
   - The raw data in CSV format is processed by the `preprocess.py` script, where missing values are handled, features are scaled, and categorical data is encoded.
   
2. **Model Training**: 
   - After preprocessing, the `train.py` script trains a machine learning model (e.g., RandomForestRegressor) using the preprocessed data.
   - The trained model is logged into **MLflow**, along with evaluation metrics such as MAE, MSE, and R² score.

3. **Model Serving**:
   - Once the model is trained, the FastAPI app (`main.py`) exposes an endpoint (`/predict`) to allow users to get predictions. The model is served from the saved MLflow artifact.
   
4. **Deployment**: 
   - The trained model is containerized using Docker and deployed to AWS EC2 using the `deploy_to_ec2.sh` script. The Docker container exposes the FastAPI app on port 80.

5. **CI/CD**:
   - **GitHub Actions** automates testing and deployment. The CI workflow runs linting and unit tests, while the CD workflow builds the Docker image and deploys it to EC2.

---

### **Next Steps:**
- **Infrastructure Diagram**: Make sure to add an actual diagram image (`architecture.png`) in the `images/` directory to visualize the system components and interactions.
- **Deployment on EC2**: Follow the EC2 deployment process using the `deploy_to_ec2.sh` script.
- **CI/CD**: Check the **GitHub Actions** workflows (`ci.yml` and `cd.yml`) to automate testing and deployment.


