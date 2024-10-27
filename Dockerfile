FROM python:latest

# Create a directory for the app
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Copy all files to the working directory
COPY . .

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Specify the command to run the application
CMD ["python", "app.py"]
