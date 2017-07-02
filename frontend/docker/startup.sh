#!/bin/sh

# Go to the project directory
cd /var/projects/frontend/angular

# Install npm dependencies
echo "Install npm dependencies"
npm install

# Run developement server
echo "Serving the angular app"
ng serve --host 0.0.0.0

exec "$@"
