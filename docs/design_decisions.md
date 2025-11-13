# Design Decisions

This document outlines the key design decisions made during the development of the MLOps project, focusing on the tools, technologies, and architectural choices that were selected to ensure efficiency, scalability, and maintainability.

## 1. **Data Versioning with DVC**

**Decision**: Use **DVC (Data Version Control)** for managing datasets and model artifacts.

### Why DVC?
- **Data Management**: DVC helps to version large datasets, ensuring that every change to the data is tracked and can be easily reproduced. This is crucial for machine learning projects, as the data is often subject to changes, and keeping track of versions allows for a clear history of the dataset.
- **Model Management**: DVC not only manages datasets but also tracks model versions, helping to manage and store machine learning models in a way that allows easy rollback to a previous version if needed.

**Alternative Considered**: Without DVC, versioning datasets and models could be done manually, but that would be error-prone and inefficient.

---

## 2. **Experiment Tracking with MLflow**

**Decision**: Use **MLflow** for tracking experiments, including hyperparameters, metrics, and model artifacts.

### Why MLflow?
- **Experiment Tracking**: MLflow allows for easy logging of model training experiments, including hyperparameters, metrics, and the resulting model. This makes it easy to compare different models and configurations, which is essential for improving model performance.
- **Model Management**: With MLflow, we can easily store and retrieve model artifacts, track different model versions, and manage the model lifecycle (e.g., deploying the best-performing model).

**Alternative Considered**: Other tools such as **Weights & Biases** were considered for experiment tracking, but MLflow was chosen due to its ease of integration and the fact that it supports multiple backend stores, including file systems, databases, and cloud solutions.

---

## 3. **FastAPI for Model Serving**

**Decision**: Use **FastAPI** to serve the trained model via an HTTP API.

### Why FastAPI?
- **Performance**: FastAPI is one of the fastest web frameworks in Python. It uses **Starlette** for the web part and **Pydantic** for data validation, making it extremely efficient.
- **Ease of Integration**: FastAPI integrates seamlessly with machine learning models, making it easy to load and serve the model via an HTTP API. This allows us to expose model predictions as a RESTful service.
- **Asynchronous Support**: FastAPI's asynchronous capabilities make it well-suited for serving machine learning models, especially when the models are called in a non-blocking manner.

**Alternative Considered**: Flask or Django could have been used, but FastAPI was selected for its superior performance and support for asynchronous requests out of the box.

---

## 4. **Containerization with Docker**

**Decision**: Use **Docker** to containerize the application, including the FastAPI model serving application.

### Why Docker?
- **Portability**: Docker containers ensure that the application runs consistently across different environments (e.g., development, testing, production). The ability to package all dependencies inside a container eliminates the "works on my machine" problem.
- **Scalability**: Docker makes it easier to scale applications. By containerizing the app, we can easily deploy it to cloud platforms or use orchestration tools like **Kubernetes** or **Docker Swarm** to scale the application as needed.
- **Ease of Deployment**: Docker simplifies the deployment process. The app can be deployed to any cloud environment (AWS EC2, GCP, Azure) without worrying about dependency conflicts or environment mismatches.

**Alternative Considered**: Other containerization tools like **Podman** were considered, but Docker is the most widely used and has robust community support.

---

## 5. **Cloud Deployment on AWS EC2**

**Decision**: Deploy the application on **AWS EC2** instances.

### Why AWS EC2?
- **Scalability**: AWS EC2 provides flexible compute resources that can be easily scaled based on demand. If the app needs more computational power, more EC2 instances can be provisioned quickly.
- **Reliability**: AWS is known for its reliability and uptime, making it a solid choice for hosting the application in production.
- **Integration with Other AWS Services**: AWS EC2 integrates seamlessly with other AWS services like **S3** (for storing datasets), **RDS** (for database storage), and **Elastic Load Balancing** (for traffic distribution).

**Alternative Considered**: **Google Cloud Platform (GCP)** and **Microsoft Azure** were also considered for hosting the application, but AWS was chosen due to its broad feature set, ease of integration with other tools, and extensive support in the machine learning ecosystem.

---

## 6. **CI/CD with GitHub Actions**

**Decision**: Use **GitHub Actions** for automating continuous integration (CI) and continuous deployment (CD).

### Why GitHub Actions?
- **Ease of Integration**: GitHub Actions integrates seamlessly with GitHub repositories, allowing for easy setup of workflows directly in the repository.
- **Automation**: GitHub Actions automates the testing and deployment pipeline, ensuring that code is tested before it is merged and that deployment happens automatically when the code is pushed to the main branch.
- **Flexibility**: With GitHub Actions, we can create custom workflows to handle linting, testing, building Docker images, and deploying to cloud platforms like AWS.

**Alternative Considered**: **Jenkins** and **GitLab CI** were considered, but GitHub Actions was chosen due to its native integration with GitHub and the ease of configuration.

---

## 7. **Data Preprocessing and Feature Engineering**

**Decision**: Perform data preprocessing and feature engineering in a dedicated module (`preprocess.py`, `make_dataset.py`, etc.).

### Why Preprocessing as a Separate Step?
- **Reproducibility**: Separating data preprocessing into its own script makes it easy to reproduce the same steps for training and evaluation, ensuring consistency in the results.
- **Modularity**: Keeping preprocessing separate allows for easier modifications to the process without affecting other parts of the pipeline. For example, if we want to add new features or change how missing values are handled, we can do so without touching the training logic.

**Alternative Considered**: Preprocessing could have been integrated directly into the model training pipeline, but separating the steps improves maintainability and scalability.

---

## 8. **Using Localstack for Local AWS Simulation**

**Decision**: Use **LocalStack** to simulate AWS services locally for testing purposes.

### Why LocalStack?
- **Cost-Effective Testing**: LocalStack allows us to simulate AWS services (like S3, DynamoDB, Lambda, etc.) on our local machine, which is useful for testing deployments and interactions without incurring cloud costs.
- **Realistic Testing Environment**: LocalStack provides a nearly identical environment to AWS, making it easier to test code locally before deploying to the actual AWS infrastructure.

**Alternative Considered**: Directly using AWS for testing could lead to increased costs and slower feedback cycles. LocalStack helps to mitigate this by allowing for local testing.

---

## Conclusion

Each of the design decisions made in this project was based on balancing ease of use, scalability, performance, and maintainability. The combination of **DVC**, **MLflow**, **FastAPI**, **Docker**, and **AWS EC2** provides a solid foundation for developing, deploying, and managing machine learning models in a production-ready MLOps pipeline.
