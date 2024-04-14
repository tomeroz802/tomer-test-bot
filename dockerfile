# Use the official Python image as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY . . 

# Install the required dependencies
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
