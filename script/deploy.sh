#!/usr/bin/env bash

#activate virtual environment
source ~/crud_venv/bin/activate

cd /var/www/CRUD-django-Docker

#pull latest codebase
git pull

#install the app dependencies
pip install -r requirements.txt

#run the db migration
python manage.py migrate

#run the collect static command
python manage.py collectstatic --no-input

#deactivate
deactivate

#reload nginx
sudo systemctl reload nginx

#restart gunicorn
sudo systemctl restart gunicorn