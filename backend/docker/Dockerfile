FROM python:3.5-onbuild

MAINTAINER Stanislav Petrov (slavpetroff@gmail.com)

################################################################################
# Environment variables           
################################################################################

# Get noninteractive frontend for Debian to avoid some problems:
# debconf: unable to initialize frontend: Dialog
ENV DEBIAN_FRONTEND noninteractive

################################################################################
# OS Updates and Python packages           
################################################################################

RUN apt-get update

RUN apt-get upgrade -y

RUN apt-get install -y

RUN apt-get install -y apt-utils

# Build dependencies for postgres
RUN apt-get install -y python-psycopg2 python3-psycopg2 python-pip python3-pip python-dev postgresql postgresql-contrib

RUN apt-get -y install binutils libproj-dev gdal-bin

################################################################################
# PIP Installs
################################################################################

RUN pip3 install asgiref
RUN pip3 install uwsgi
RUN pip3 install -r requirements.txt

# Create workdir
RUN mkdir -p /var/projects/backend/docker

# Move docker files to a folder in the container
COPY ./ /var/projects/backend/docker/

# Set workdir
WORKDIR /var/projects/backend

# List working directory`s files
RUN ls -a /var/projects/backend/docker/

# Make startup script executable
RUN chmod +x "docker/startup.sh"

################################################################################
# Run startup.sh script when the container starts.                               
# Note: If you run migrations etc outside ENTRYPOINT, envs won't be available! 
################################################################################

ENTRYPOINT ["docker/startup.sh"]

# Expose container's port
EXPOSE 8080
