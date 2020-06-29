from celery import shared_task
from django.contrib.auth.forms import PasswordResetForm

from accounts.models import Employee


@shared_task
def send_mail(subject_template_name, email_template_name, context,
              from_email, to_email, html_email_template_name):
    context['user'] = Employee.objects.get(user_id=context['user']).user

    PasswordResetForm.send_mail(
        None,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name
    )
    return 'Password reset link has been sent!'
