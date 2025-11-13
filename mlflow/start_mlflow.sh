#!/bin/bash

# Script to start MLflow server using Docker Compose
echo "Starting MLflow server..."

# Run Docker Compose in detached mode to start the MLflow server
docker-compose -f mlflow/docker-compose.yml up -d

# Give the server a few seconds to start
echo "Waiting for MLflow server to start..."
sleep 5

# Verify if the MLflow server is running
if docker ps | grep -q "mlflow-server"; then
    echo "MLflow server is up and running!"
    echo "Access the MLflow UI at http://localhost:5000"
else
    echo "Error: MLflow server failed to start."
    exit 1
fi
