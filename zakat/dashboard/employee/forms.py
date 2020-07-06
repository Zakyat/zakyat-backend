from django import forms
from accounts.models import Employee
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=True)
        return user


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ("user",)

    def save(self, user, commit=True):
        employee = Employee()
        employee.user = user
        employee.position = self.cleaned_data['position']
        employee.phone_number = self.cleaned_data['phone_number']
        employee.bio = self.cleaned_data['bio']
        employee.photo = self.cleaned_data['photo']

        if commit:
            employee.save()

