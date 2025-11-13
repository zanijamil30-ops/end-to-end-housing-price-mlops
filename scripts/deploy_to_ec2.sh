#!/bin/bash

# Set EC2 details
EC2_USER="ubuntu"                  # EC2 instance user
EC2_HOST="your-ec2-public-ip"      # Public IP address of EC2
EC2_KEY_PATH="/path/to/your/ssh/key.pem"  # Path to your EC2 private key

# Path to your Docker image and application directory
DOCKER_IMAGE="mlops-portfolio"
APP_DIRECTORY="/home/ubuntu/mlops-portfolio"

# SSH into EC2 and run commands
echo "Deploying to EC2 instance..."
ssh -i $EC2_KEY_PATH $EC2_USER@$EC2_HOST << EOF
    # Navigate to the project directory
    cd $APP_DIRECTORY

    # Pull the latest changes from Git (optional)
    git pull origin main

    # Build the Docker image
    docker build -t $DOCKER_IMAGE .

    # Run the Docker container
    docker run -d -p 80:8000 $DOCKER_IMAGE

    # Confirm that the container is running
    docker ps
EOF

echo "Deployment to EC2 complete!"
