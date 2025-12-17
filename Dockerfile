# 1. Base image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Install minimal system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy dependency list first (layer caching)
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy application code
COPY app app

# 7. Expose port (default 8000, can be overridden)
ENV PORT=9000
EXPOSE ${PORT}

# 8. Run FastAPI with environment variables
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT