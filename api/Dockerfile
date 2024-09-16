FROM python:3.12.6-bookworm
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy requirements.txt into the container
WORKDIR /api
COPY requirements.txt .

# Install dependencies into the container
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin lsb-release iputils-ping \
    && sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' \
    && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && apt-get update && apt-get install -yqq --no-install-recommends postgresql-client-16 \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .
EXPOSE 8000
