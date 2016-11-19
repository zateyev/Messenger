release: python manage.py makemigrations messages_
release: python manage.py makemigrations registrar
release: python manage.py migrate
web: gunicorn messenger.wsgi --log-file -
