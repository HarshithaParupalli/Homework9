# Use an official Python image with a lightweight variant for efficiency
FROM python:3.12-slim-bullseye AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

# Install necessary system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure the start.sh script has executable permissions
RUN chmod +x /app/start.sh

# Expose the application port
EXPOSE 8000

# Use start.sh as the default command
CMD ["/app/start.sh"]
