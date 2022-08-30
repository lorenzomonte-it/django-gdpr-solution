#!/bin/bash

current_directory="$( pwd; )";

echo "Start create project..."
sleep 2

mkdir ./src
cd src

python3 -m venv env
. env/bin/activate
pip install --upgrade pip
pip install django

django-admin startproject django_settings .

echo "...create symbolic link..."
sleep 2
ln -s $current_directory/gdpr_solution .

echo "...make migrations..."
sleep 2
python manage.py makemigrations
python manage.py migrate

echo "...Finish"\n\n

echo "NEXT STEPS:"
echo "- Activate virtual environment"
echo "- Add 'gdpr-solution' to INSTALLED_APPS"
echo "- Run 'makemigrations' and 'migrate'"
echo "- Create superuser"