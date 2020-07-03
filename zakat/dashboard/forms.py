from django import forms
from django.contrib.auth.forms import PasswordResetForm as PasswordResetFormCore
from multiupload.fields import MultiFileField

from news.models import Post, PostTag, PostImage
from .tasks import send_mail


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
