#!/bin/bash
# Build and deploy model as a Docker container

echo "Building Docker image..."
docker build -t fraud-detection:latest .

echo "Running Docker container..."
docker run -d -p 5000:5000 fraud-detection:latest

echo "Fraud detection service deployed at http://localhost:5000"
