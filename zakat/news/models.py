from djongo import models

from projects.models import Project
from accounts.models import Employee


class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.TextField()    # TODO: i18n
	description = models.TextField()    # TODO: i18n
	project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
	created_by = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
	# TODO: Decide whether social links are needed to be stored here


class PostImage(models.Model):
	image = models.ImageField(upload_to='uploads')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')


class PostTag(models.Model):
	tag = models.CharField(max_length=16)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags')

