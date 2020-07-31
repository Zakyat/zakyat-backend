from django import forms
from accounts.models import Employee
from django.contrib.auth.models import User, Permission
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

class UserForm(forms.ModelForm):
    content_type = ContentType.objects.get_for_model(User)
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects,
        widget=forms.CheckboxSelectMultiple,
        required=False)

    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = "__all__"

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        user.save()
        return user


class UserEditForm(forms.ModelForm):
    user_id = forms.IntegerField(widget=forms.HiddenInput)
    content_type = ContentType.objects.get_for_model(User)
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects,
        widget=forms.CheckboxSelectMultiple,
        required=False)

    class Meta:
        model = User
        fields = "__all__"
        exclude = ('password',)

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


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

#
# class UpdatePasswordForm(forms.ModelForm):
#     pass