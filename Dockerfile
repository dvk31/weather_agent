# Use a base image with Python 3.11
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the FastAPI application
CMD ["uvicorn", "hello_fastapi.main:app", "--host", "0.0.0.0", "--port", "80"]


