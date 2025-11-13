#!/bin/bash

# Build the Docker image for the application
echo "Building Docker image..."
docker build -t mlops-portfolio .

# Check if the image was built successfully
if [ $? -ne 0 ]; then
    echo "Docker image build failed! Exiting."
    exit 1
fi

# List Docker images to verify
docker images

echo "Docker image built successfully."
