from django.contrib import admin

from .models import Project, Request


admin.site.register(Request)
admin.site.register(Project)
