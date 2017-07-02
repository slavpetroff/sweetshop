#!/bin/sh

# Create a log directory if it is not existing, otherwise delete the old one
# and recreate it. This way we always get the new logs and protect ourselves 
# from exceptions in the Docker`s daemon
if [ ! -d /var/app/entryscript_logs ]; then
  mkdir /var/app/entryscript_logs 
fi

# Install PIP requirements
echo "Installing PIP requirements"
pip install -r /var/projects/backend/django/requirements.txt

# Collect static files
echo "Collect static files"
python /var/projects/backend/django/manage.py collectstatic --noinput >> /var/app/entryscript_logs/collectstatics.txt  

# Make database migrations
echo "Make database migrations"
python /var/projects/backend/django/manage.py makemigrations >> /var/app/entryscript_logs/makemigrations.txt

# Apply database migrations
echo "Apply database migrations"
python /var/projects/backend/django/manage.py migrate >> /var/app/entryscript_logs/migrate.txt

# Serve the Django app
/usr/local/bin/uwsgi --ini /var/projects/backend/docker/uwsgi.ini

exec "$@"
