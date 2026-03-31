# Dockerfile for FastAPI Application

# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Set the environment variable for FastAPI
ENV UVICORN_CMD='uvicorn main:app --host 0.0.0.0 --port 8000 --reload'

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["sh", "-c", "$UVICORN_CMD"]