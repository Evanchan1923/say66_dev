# Use an official Python 3.12 runtime as a parent image
FROM python:3.12-slim

# Set environment variables
# 禁止 Python 写入 pyc 文件到磁盘，
# 设置 Python 的输出为非缓冲模式
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies for git and build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    gnupg \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Git LFS
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
    apt-get install -y git-lfs && \
    git lfs install

# Clone the GitHub repository (replace with your repo URL)
ARG REPO_URL=https://github.com/Evanchan1923/say66_dev
ARG BRANCH=main
RUN git clone --branch $BRANCH $REPO_URL /app
RUN git lfs pull

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 6000

# Command to run the FastAPI service using uvicorn
# 使用 uvicorn 运行 FastAPI 服务，监听所有 IP 的 8000 端口
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "6000"]

