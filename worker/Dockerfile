FROM python:3.12.6-bookworm
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy requirements.txt into the container
WORKDIR /worker
COPY requirements.txt .

# Install dependencies into the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .
CMD ["bash", "run_celery.sh"]
