# Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command: run the pipeline with example initial parameters
CMD ["python", "-m", "app.pipeline", "--initial_params", "0.1,0.1,0.1"]
