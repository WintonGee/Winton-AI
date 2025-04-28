# Winton Gee - AI-Powered Portfolio Chatbot

[![chatbot.wintongee.com](https://chatbot.wintongee.com)](https://chatbot.wintongee.com)

[![Deploy to Google Cloud Run](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

An intelligent chatbot that answers questions about my professional experience using AI.
Deployed on Google Cloud Run with Docker for scalable, serverless hosting.

## 🛠️ Technologies Used

### Core Stack

| Technology           | Purpose                     | Version          |
| -------------------- | --------------------------- | ---------------- |
| **Python**           | Main programming language   | 3.9+             |
| **LangChain**        | LLM orchestration framework | 0.3.19           |
| **Hugging Face**     | Sentence embeddings         | all-MiniLM-L6-v2 |
| **FAISS**            | Vector similarity search    | 1.7.4            |
| **Ollama**           | Local LLM execution         | 0.1.27           |
| **Gradio**           | Web interface               | 3.50.2           |
| **Docker**           | Containerization            | 24.0+            |
| **Google Cloud Run** | Serverless hosting          | -                |

### Key Components

1. **Resume Processing Pipeline**

   - PDF text extraction with PyPDF2
   - Text chunking using LangChain's RecursiveTextSplitter
   - FAISS vector store for efficient similarity search

2. **AI Architecture**

   - Retrieval-Augmented Generation (RAG) pattern
   - Mistral-7B LLM via Ollama (Currently configuring DeepSeek R1)
   - Custom prompt engineering for interview responses

3. **Deployment**
   - Docker containerization
   - Serverless scaling with Google Cloud Run
   - Automatic HTTPS via Google's global load balancer

## 📋 Prerequisites

1. **Accounts**

   - [Google Cloud Account](https://console.cloud.google.com/) (Free $300 credit)
   - [Docker Hub](https://hub.docker.com/) (Optional for custom images)

2. **Local Development Tools**
   ```bash
   # Minimum versions
   Python 3.9+
   Docker 24.0+
   Ollama 0.1.27+
   Google Cloud CLI 464.0+
   ```
