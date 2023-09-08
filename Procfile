web: gunicorn drf_api.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --upload-unhashed-files
release: python manage.py migrate --noinput