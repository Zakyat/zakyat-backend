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


class UserEditForm(UserForm):
    user_id = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data['username']
        user_id = cleaned_data['user_id']
        print('user_id - ', user_id)
        try:
            user = User.objects.get(username=username)
            if user.id != user_id:
                raise forms.ValidationError('User with this username already exists')
        except User.DoesNotExist:
            return cleaned_data
        return cleaned_data

    def save(self, commit=True):
        print('cleaned_data', self.cleaned_data)
        user_id = self.cleaned_data.pop('user_id')
        user_permissions = self.cleaned_data.pop('user_permissions')
        groups = self.cleaned_data.pop('groups')
        print('cleaned_data', self.cleaned_data)
        User.objects.filter(id=user_id).update(**self.cleaned_data)
        user = User.objects.get(id=user_id)
        for group in groups:
            user.groups.add(group)
        for permissions in user_permissions:
            user.user_permissions.add(permissions)
        user.save()
        return user

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ("user",)

    def save(self, user, edit=False):
        if isinstance(user, User):
            if edit == False:
                employee = Employee()
                employee.user = user
                employee.position = self.cleaned_data['position']
                employee.phone_number = self.cleaned_data['phone_number']
                employee.photo = self.cleaned_data['photo']
                employee.save()
            else:
                Employee.objects.filter(user=user).update(**self.cleaned_data)


