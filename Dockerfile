# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY ./app/ /app/

# Specify which port it runs on- note the "run" command will be what actually opens the ports
EXPOSE 8050

# Specify the command to run on container start
CMD ["python", "dash_app.py"]