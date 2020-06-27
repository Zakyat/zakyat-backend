from django import forms
from accounts.models import Employee

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

    def save(self, commit=True):
        employee = Employee()
        employee.user = self.cleaned_data['user']
        employee.phone_number = self.cleaned_data['phone_number']
        employee.photo = self.cleaned_data['photo']
        position = self.cleaned_data['position']

        if commit:
         employee.save()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
