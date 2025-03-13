# Use ultra-light Alpine base
FROM python:3.9-alpine

# Install only essential system dependencies
RUN apk update && apk add --no-cache \
    curl \
    g++ \
    make \
    libc-dev \
    linux-headers

# Install Ollama (lightweight method)
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Set working directory
WORKDIR /app

# Copy only necessary files
COPY requirements.txt .
COPY app ./app
COPY data/processed/resume_chunks.json ./data/processed/
COPY scripts ./scripts

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Use smaller model (1.8GB vs 4.1GB)
RUN ollama pull phi3

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s \
  CMD curl --fail http://localhost:11434 || exit 1

# Start with delay for Ollama initialization
CMD ollama serve > /dev/null 2>&1 & \
    sleep 25 && \
    python app/chatbot.py