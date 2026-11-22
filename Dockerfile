
# Stage 1: Build React
FROM node:22-alpine AS frontend-builder

WORKDIR /app/frontend

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ ./
RUN npm run build


# Stage 2: Run FastAPI + React
FROM python:3.11-slim

WORKDIR /app

# Install backend dependencies
COPY backend/requirements.txt backend/requirements.txt

RUN pip install --no-cache-dir \
    -r backend/requirements.txt

# Copy backend
COPY backend/ backend/

# Copy compiled React frontend
COPY --from=frontend-builder \
    /app/frontend/dist /app/frontend/dist

# Expose application port
EXPOSE 7860

# Start FastAPI
CMD ["uvicorn", "backend.app.main:app", \
     "--host", "0.0.0.0", "--port", "7860"]
