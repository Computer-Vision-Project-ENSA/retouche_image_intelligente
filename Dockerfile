
# Stage 1: Build React frontend
FROM node:22-alpine AS frontend-builder

WORKDIR /app/frontend

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ ./
RUN npm run build


# Stage 2: FastAPI application
FROM python:3.11-slim

WORKDIR /app

# Install backend dependencies
COPY backend/requirements.txt backend/requirements.txt

RUN pip install --no-cache-dir \
    -r backend/requirements.txt

# Copy backend
COPY backend/ backend/

# Copy React production build
COPY --from=frontend-builder \
    /app/frontend/dist /app/frontend/dist

# FastAPI serves React and API on the same port
EXPOSE 7860

CMD ["uvicorn", "backend.app.main:app", \
     "--host", "0.0.0.0", "--port", "7860"]
