from django import forms
from django.contrib.auth.forms import PasswordResetForm as PasswordResetFormCore
from .tasks import send_mail


class PasswordResetForm(PasswordResetFormCore):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(
        attrs={
            'id': 'email',
            'placeholder': 'Email'
        }
    ))

    def send_mail(self, subject_template_name, email_template_name, context,
                  from_email, to_email, html_email_template_name=None):
        context['user'] = context['user'].id
        send_mail.delay(subject_template_name=subject_template_name,
                        email_template_name=email_template_name,
                        context=context, from_email=from_email, to_email=to_email,
                        html_email_template_name=html_email_template_name)
