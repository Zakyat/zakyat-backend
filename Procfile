web: gunicorn zakat.wsgi --log-file -
worker: celery worker -A zakat --beat -l info --pool=solo