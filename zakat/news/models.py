from djongo import models
from projects.models import Project
from accounts.models import Employee


class Post(models.Model):
	title = models.TextField()    # TODO: i18n
	description = models.TextField()    # TODO: i18n
	project = models.OneToOneField(Project, null=True, on_delete=models.SET_NULL)
	created_by = models.OneToOneField(Employee, null=True, on_delete=models.SET_NULL)
	# TODO: Decide whether social links are needed to be stored here
	images = models.ArrayField(model_container=models.ImageField())
	tags = models.ArrayField(model_container=models.CharField(max_length=16))
