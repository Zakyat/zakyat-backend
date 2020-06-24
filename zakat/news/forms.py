from django import forms

from . import models


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = models.Post
        exclude = ()