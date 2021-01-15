python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py flush --no-input
python manage.py migrate
uwsgi --http :8000 --module wsgi