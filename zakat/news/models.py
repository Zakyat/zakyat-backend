from djongo import models

from markdownx.models import MarkdownxField
from projects.models import Project
from accounts.models import Employee
from martor.models import MartorField


class PostTag(models.Model):
	name = models.CharField(max_length=16)

	def __str__(self):
		return self.name


class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.TextField()    # TODO: i18n
	description = MartorField()    # TODO: i18n
	
	project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
	created_by = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
	tags = models.ManyToManyField(PostTag)
	# TODO: Decide whether social links are needed to be stored here
	def __str__(self):
		return self.title


class PostImage(models.Model):
	image = models.ImageField(upload_to='uploads')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
