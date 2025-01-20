# Use an official Python 3.12 runtime as a parent image
FROM python:3.12-slim

# Set environment variables
# 禁止 Python 写入 pyc 文件到磁盘，设置 Python 的输出为非缓冲模式
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies for git and build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    gnupg \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Git LFS
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
    apt-get install -y --no-install-recommends git-lfs && \
    git lfs install && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone the GitHub repository (replace with your repo URL)
ARG REPO_URL=https://github.com/Evanchan1923/say66_dev
ARG BRANCH=main
RUN git clone --branch $BRANCH $REPO_URL /app && \
    cd /app && git lfs pull

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the FastAPI app will run on
EXPOSE 5000

# Command to run the FastAPI service using uvicorn
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]

CMD ["python", "app.py"]