from __future__ import absolute_import, unicode_literals
import django
from django.core.management import call_command
from django.db.utils import OperationalError
# try:
#     django.setup()
#     call_command("migrate", interactive=False)
# except OperationalError as exc:
#     print("Couldn't apply migrations:", exc)

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)