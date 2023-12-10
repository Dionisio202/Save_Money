#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Ejecuta el comando para aplicar las migraciones
python manage.py migrate

# Crea un superusuario (sustituye 'superuser' por los valores que desees)
#echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('dionisio202', 'solisedison@outlook.com', 'EdisonsolIs202.')" | python manage.py shell

# Recoge archivos estáticos
python manage.py collectstatic --no-input
