FROM python:latest

# Create a directory for the app
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Copy all files to the working directory
COPY . .

EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV FLASK_ENV=production

# Run the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
