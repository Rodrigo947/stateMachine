#!/bin/sh

apt install postgresql-client -y
 
until PGPASSWORD=$POSTGRES_PASSWORD psql -h $POSTGRES_HOST -U $POSTGRES_USER -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
  
apt remove postgresql-client -y

>&2 echo "Postgres is up - executing command"

python manage.py migrate
python manage.py createsuperuser --noinput --email $DJANGO_SUPERUSER_EMAIL --cpf 11111111111 --pis 22222222222 --password $DJANGO_SUPERUSER_PASSWORD 
python manage.py runserver 0.0.0.0:$DJANGO_PORT