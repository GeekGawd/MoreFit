web: gunicorn morefit.wsgi
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
heroku ps:scale web=1