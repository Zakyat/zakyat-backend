from django.contrib import admin

from .models import Project, Request, Campaign


admin.site.register(Request)
admin.site.register(Project)
admin.site.register(Campaign)
