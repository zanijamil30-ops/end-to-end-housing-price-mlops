# Production Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for model serving and minimal tools
RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install Python dependencies
COPY src/app/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ /app/

# Expose port for FastAPI (or any other web framework)
EXPOSE 8080

# Command to run FastAPI (adjust if using another framework)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

