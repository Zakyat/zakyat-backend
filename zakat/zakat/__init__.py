import django
from django.core.management import call_command
from django.db.utils import OperationalError
try:
    django.setup()
    call_command("migrate", interactive=False)
except OperationalError as exc:
    print("Couldn't apply migrations:", exc)
