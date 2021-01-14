python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --no-input
uwsgi --http :8000 --module wsgi