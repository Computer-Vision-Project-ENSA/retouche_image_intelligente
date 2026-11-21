
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY backend/requirements.txt backend/requirements.txt
COPY frontend/requirements.txt frontend/requirements.txt

RUN pip install --no-cache-dir \
    -r backend/requirements.txt \
    -r frontend/requirements.txt

# Copy application code
COPY backend/ backend/
COPY frontend/ frontend/

# Configure Gradio -> FastAPI communication
ENV API_URL=http://127.0.0.1:7860/api/process

EXPOSE 7860

# Start the application
CMD ["uvicorn", "backend.app.main:app", \
     "--host", "0.0.0.0", "--port", "7860"]
