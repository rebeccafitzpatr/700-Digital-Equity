FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y iputils-ping gcc

# Set workdir
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Start your app
CMD ["python", "Web.py"]