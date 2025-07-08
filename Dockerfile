# Use official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies for Playwright + xvfb for virtual display
RUN apt-get update && \
    apt-get install -y \
        wget gnupg curl unzip \
        libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 \
        libxss1 libgtk-3-0 libasound2 \
        xvfb libx11-xcb1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Playwright browsers
RUN python -m playwright install --with-deps

# Set entrypoint command
CMD ["pytest", "--alluredir=allure-results"]
