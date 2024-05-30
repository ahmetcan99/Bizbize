# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /Bizbize

# Add the current directory contents into the container at /app
ADD . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME Bizbize

# Run app.py when the container launches
CMD ["gunicorn", "Bizbize.wsgi:application", "--bind", "0.0.0.0:80"]