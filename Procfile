web: gunicorn zakat.zakat.wsgi --log-file -
worker: celery worker -A zakat.zakat --beat -l info --pool=solo