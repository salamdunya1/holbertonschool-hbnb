# Use an appropriate Alpine Linux base image with Python 3.9
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_PORT 5000

# Set the working directory in the container
WORKDIR /app

# Install system dependencies and build tools
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev openssl-dev postgresql-dev

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application source code into the container
COPY . /app

# Create a volume for persistent data
VOLUME /app/data

# Expose the application port
EXPOSE $APP_PORT

# Command to run the application with Gunicorn
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 $APP_PORT your_application_module_name:app"]
