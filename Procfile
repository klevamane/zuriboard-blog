release: python manage.py migrate
web: gunicorn blog.wsgi --log-file - --log-level debug
