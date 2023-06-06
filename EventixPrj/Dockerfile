# Base image
FROM python:3.9

# Set work directory
WORKDIR /app

# Update libpq library
RUN apt-get update && apt-get install -y libpq-dev

# Copy requirements file
COPY requirements.txt .

# Install dependencies

RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables (if needed)


# Expose port (if needed)
EXPOSE 8000

# Define the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
