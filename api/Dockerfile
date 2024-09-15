
FROM python:3.12.6-bookworm
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Copy requirements.txt into the container
WORKDIR /api
COPY requirements.txt .
# Install dependencies into the container
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin\
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .
EXPOSE 8000