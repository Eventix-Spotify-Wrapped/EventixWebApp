# Base image
FROM python:3.9

# Set work directory
WORKDIR /app

# Update system packages and install libpq for PostgreSQL connection
RUN apt-get update && apt-get install -y libpq-dev

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Upgrade psycopg2-binary library
RUN pip install --upgrade psycopg2-binary

# Install Node.js and npm
RUN apt-get install -y nodejs npm

# Install your Node.js dependencies

COPY . .
#COPY package.json .
#COPY package-lock.json .
#COPY webpack.mix.js .
RUN npm install


RUN npm run prod


# Expose port (if needed)
EXPOSE 8000

# Define the command to run the application
CMD ["gunicorn", "EventixPrj.wsgi:application", "--bind", "0.0.0.0:8000"]
