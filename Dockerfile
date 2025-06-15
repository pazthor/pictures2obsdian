# Multi-stage build: Frontend build stage
FROM node:18-alpine AS frontend-builder

# Set working directory for frontend
WORKDIR /app/frontend

# Copy package files
COPY frontend/package*.json ./
# Install dependencies
RUN npm install

# Copy frontend source
COPY frontend/ ./

# Build the React app
RUN npm run build

# Backend stage
FROM python:3.11-slim

# Set working directory
WORKDIR /app
RUN mkdir api_vault
# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy environment file and backend requirements
COPY .env ./back_end/
COPY back_end/requirements.txt ./back_end/
# Install Python dependencies
RUN pip install -r back_end/requirements.txt

# Copy backend source
COPY back_end/ ./back_end/

# Copy built frontend from frontend-builder stage
COPY --from=frontend-builder /app/frontend/build ./frontend/build

# Expose port
EXPOSE 8000

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=11

# Run the application
CMD ["python", "back_end/main.py"]