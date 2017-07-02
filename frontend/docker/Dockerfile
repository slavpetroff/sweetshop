FROM ubuntu:latest

MAINTAINER Stanislav Petrov (slavpetroff@gmail.com)

################################################################################
# Environment variables           
################################################################################

# Get noninteractive frontend for Debian to avoid some problems:
# debconf: unable to initialize frontend: Dialog
ENV DEBIAN_FRONTEND noninteractive

################################################################################
# Update OS
################################################################################

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y

RUN apt-get install -y apt-utils 

RUN apt-get install -y nano wget

RUN apt-get -y install binutils libproj-dev gdal-bin build-essential

RUN apt-get install -y python-software-properties

################################################################################
# Install Nodejs and Npm stuffs
################################################################################

RUN sed -i -e 's/us.archive.ubuntu.com/archive.ubuntu.com/g' /etc/apt/sources.list

RUN apt-get update && apt-get install curl -y
 
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash
RUN apt-get install -y nodejs
RUN apt-get install -y build-essential
RUN echo Installing source NPM dependencies...

ENV PATH $PATH:/nodejs/bin

RUN npm install -g @angular/cli

################################################################################
# Container specific action
################################################################################

# Create workdir
RUN mkdir -p /var/projects/frontend/docker

# List current directory`s files
RUN ls -a

# Move docker files to a folder in the container
COPY ./ /var/projects/frontend/docker/

# Set workdir
WORKDIR /var/projects/frontend

# List working directory`s files
RUN ls -a /var/projects/frontend/docker/

# Make startup script executable
RUN chmod +x "/var/projects/frontend/docker/startup.sh"

################################################################################
# Run startup.sh script when the container starts.                               
# Note: If you run migrations etc outside ENTRYPOINT, envs won't be available! 
################################################################################

ENTRYPOINT ["/var/projects/frontend/docker/startup.sh"]

# Expose container's port
EXPOSE 4200
