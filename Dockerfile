FROM python:3.9-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    curl \
    g++ \
    make \
    gcc \
    tini

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

WORKDIR /app

# Copy requirements first for layer caching
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy application files
COPY . .

# Empty layer for model (pull at runtime)
RUN echo "Model will be downloaded at runtime" 

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s \
  CMD curl --fail http://localhost:11434 || exit 1

# Start command
CMD ["tini", "--", "sh", "-c", \
    "ollama serve > /dev/null 2>&1 & \
    sleep 15 && \
    ollama pull phi3 && \
    sleep 30 && \
    python app/chatbot.py"]