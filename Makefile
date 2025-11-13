# Makefile for automating tasks in the MLOps project

# Project variables
DOCKER_IMAGE_NAME = mlops_project
DOCKER_DEV_IMAGE_NAME = mlops_project_dev
PYTHON = python3
PIP = pip
DVC = dvc
TEST_COMMAND = pytest

# Install dependencies
install:
	$(PIP) install -r requirements.txt

# Install development dependencies (including tools like pytest, linters)
install-dev:
	$(PIP) install -r requirements-dev.txt

# Initialize DVC and pull data (if DVC is being used for version control)
dvc-init:
	$(DVC) init
	$(DVC) remote add -d myremote s3://my-bucket/path/to/dvc
	$(DVC) pull

# Build the Docker image for the production environment
build:
	docker build -t $(DOCKER_IMAGE_NAME) -f docker/Dockerfile .

# Build the Docker image for the development environment (includes Jupyter and debug tools)
build-dev:
	docker build -t $(DOCKER_DEV_IMAGE_NAME) -f docker/Dockerfile.dev .

# Run tests locally
test:
	$(TEST_COMMAND)

# Lint the codebase
lint:
	flake8 src/ tests/ --max-line-length=120

# Run all tasks (install dependencies, run tests, and lint)
run-all: install lint test

# Run the FastAPI server
serve:
	uvicorn src.app.main:app --reload

# Clean up the Docker containers and images
clean:
	docker system prune -f

# Run the full DVC pipeline (from data preprocessing to model training)
dvc-repro:
	$(DVC) repro

# Start the Prometheus server to monitor metrics (assuming the configuration is set)
prometheus:
	prometheus --config.file=monitoring/prometheus/example.yml

# Deploy the application to an AWS EC2 instance (uses SSH)
deploy-ec2:
	./scripts/deploy_to_ec2.sh

# Clean up Python bytecode files
clean-pyc:
	find . -name "*.pyc" -exec rm -f {} \;

# Push the Docker image to the registry (if using Docker Hub or private registry)
docker-push:
	docker push $(DOCKER_IMAGE_NAME)

# Show Docker images
docker-images:
	docker images

# Start MLflow server
start-mlflow:
	./mlflow/start_mlflow.sh
