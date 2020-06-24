from django.forms import PasswordInput

from . import models
from django import forms


class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        exclude = ('user',)


class EmployeeAuthorizationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput())