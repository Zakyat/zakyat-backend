from django import forms
from djongo import models

from projects.models import Project
from accounts.models import Employee


class ImageModel(models.Model):
	image = models.ImageField(upload_to='uploads')


class TagModel(models.Model):
	tag = models.CharField(max_length=16)


class ImageModelForm(forms.ModelForm):
	class Meta:
		model = ImageModel
		exclude = ()


class TagModelForm(forms.ModelForm):
	class Meta:
		model = TagModel
		exclude = ()


class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.TextField()    # TODO: i18n
	description = models.TextField()    # TODO: i18n
	project = models.OneToOneField(Project, null=True, on_delete=models.SET_NULL)
	created_by = models.OneToOneField(Employee, null=True, on_delete=models.SET_NULL)
	# TODO: Decide whether social links are needed to be stored here
	images = models.ArrayField(model_container=ImageModel, model_form_class=ImageModelForm)
	tags = models.ArrayField(model_container=TagModel, model_form_class=TagModelForm)
