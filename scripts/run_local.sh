#!/bin/bash

# Run the DVC pipeline and train the model
echo "Running DVC pipeline..."
dvc repro

# Check if the DVC pipeline was successful
if [ $? -ne 0 ]; then
    echo "DVC pipeline failed! Exiting."
    exit 1
fi

# Train the model if DVC pipeline was successful
echo "Training the model..."
python src/model/train.py

# Check if the model training was successful
if [ $? -ne 0 ]; then
    echo "Model training failed! Exiting."
    exit 1
fi

# Serve the model locally using FastAPI
echo "Starting FastAPI server..."
uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload

# Check if the FastAPI server started successfully
if [ $? -ne 0 ]; then
    echo "FastAPI server failed to start! Exiting."
    exit 1
fi
