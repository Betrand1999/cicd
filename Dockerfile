# FROM python:3.9-slim

# WORKDIR /app
# RUN pip install flask

# # Copy only the .whl package from dist/
# COPY dist/*.whl /app/

# # Install the package
# RUN pip install /app/*.whl

# # Expose port 8000
# EXPOSE 8000

# # Run the Flask application
# CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]

# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["python", "hello_world_app/app.py"]
