# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Check internet connectivity
RUN apt-get update && apt-get install -y curl && curl -I https://pypi.org
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*



# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME PanicPortal

# Run app.py when the container launches
CMD ["python", "bot.py"]
