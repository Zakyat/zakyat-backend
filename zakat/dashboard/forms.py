from django import forms
from multiupload.fields import MultiImageField, MultiFileField

from accounts.models import Employee
from news.models import Post, PostTag, PostImage


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


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ()

    images = MultiFileField(min_num=0, max_num=10, attrs={'accept': 'image/*'})
    tags = forms.CharField(label='Tags (separate them with a comma)')

    def save(self, commit=True):
        instance = super(PostCreateForm, self).save(commit)
        for each in self.cleaned_data['images']:
            PostImage.objects.create(image=each, post=instance)

        tags = self.cleaned_data['tags'].replace(' ', '').split(',')
        for tag in tags:
            PostTag.objects.create(tag=tag, post=instance)
        return instance


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('created_at', 'created_by',)

    images = MultiFileField(min_num=0, max_num=10, attrs={'accept': 'image/*'})
    tags = forms.CharField(label='Tags (separate them with a comma)')

    def save(self, commit=True):
        instance = super(PostEditForm, self).save(commit)
        for image in PostImage.objects.filter(post=instance).all():
            image.delete()
        for each in self.cleaned_data['images']:
            PostImage.objects.create(image=each, post=instance)

        for tag in PostTag.objects.filter(post=instance).all():
            tag.delete()
        tags = self.cleaned_data['tags'].replace(' ', '').split(',')
        for tag in tags:
            PostTag.objects.create(tag=tag, post=instance)
        return instance
