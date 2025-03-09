FROM python:3.9-slim

WORKDIR /app

# Define a build argument for the latest artifact (to be passed in during the build)
ARG LATEST_WHL

# Copy the dynamically created artifact (Python wheel package) into the container
COPY dist/${LATEST_WHL} /app/

# Install the package inside the container
RUN pip install /app/${LATEST_WHL}

# Expose port 8000
EXPOSE 8000

# Run the Flask application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]
