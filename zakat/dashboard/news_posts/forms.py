from django import forms
# from multiupload.fields import MultiFileField
from markdownx.fields import MarkdownxFormField
from martor.fields import MartorFormField

from news.models import Post, PostTag, PostImage
from projects.models import Project

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('created_by',)

    # images = MultiFileField(min_num=0, max_num=10, attrs={'accept': 'image/*'})
    tags = forms.ModelMultipleChoiceField(queryset=PostTag.objects.all())
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))  # TODO: i18n
    description = MartorFormField()
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.Select(attrs={'class': 'select'}))
    # def save(self, user):
    #     instance = super(PostCreateForm, self).save()
    #     instance.user = user
    #     for each in self.cleaned_data['images']:
    #         PostImage.objects.create(image=each, post=instance)
    #
    #     tags = self.cleaned_data['tags'].replace(' ', '').split(',')
    #     for tag in tags:
    #         PostTag.objects.create(tag=tag, post=instance)
    #     return instance


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('created_at', 'created_by',)

    # images = MultiFileField(min_num=0, max_num=10, attrs={'accept': 'image/*'})
    description = MarkdownxFormField()
    tags = forms.ModelMultipleChoiceField(queryset=PostTag.objects.all())

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