FROM python:3.9-slim

WORKDIR /app

# Copy only the .whl package from dist/
COPY dist/*.whl /app/

# Install the package
RUN pip install /app/*.whl

# Expose port 8000
EXPOSE 8000

# Run the Flask application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]
