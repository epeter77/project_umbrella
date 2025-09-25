# Dockerfile for PROJECT_UMBRELLA Django Application

# Stage 1: Define the base image. We'll use an official Python image.
# This gives us a lightweight Linux environment with Python pre-installed.
FROM python:3.11-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container.
# All subsequent commands will run from this directory.
WORKDIR /app

# Copy the file that lists our Python dependencies into the container.
COPY requirements.txt /app/

# Install the dependencies. We are installing them before copying the rest
# of the code because these change less often, allowing Docker to cache this layer.
RUN pip install --no-cache-dir -r requirements.txt

# Now, copy the rest of our application's code into the container.
COPY . /app/

# The port the container will listen on. We'll use 8000, the Django default.
EXPOSE 8000

# The command to run when the container starts.
# We use gunicorn as it's a production-ready web server, unlike Django's runserver.
# NOTE: You will need to add 'gunicorn' to your requirements.txt file!
CMD ["sh", "-c", "gunicorn project_umbrella.wsgi:application --bind 0.0.0.0:$PORT"]
