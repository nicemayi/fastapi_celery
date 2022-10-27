# Use an official Python runtime as a parent image
FROM python:3.10.8-alpine3.16

# RUN apt-get update && apt-get install -y --no-install-recommends gcc musl-dev libc-dev python-setuptools
COPY requirements.txt /app/requirements.txt
# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# && apt-get purge -y --auto-remove gcc
# apt-get update \
# && apt-get install -y --no-install-recommends gcc \
#  && rm -rf /var/lib/apt/lists/* \

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 8000
EXPOSE 5566

