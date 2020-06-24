from django.contrib import auth
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

from accounts.models import Employee


class EmployeePermissionMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        employee = Employee.objects.get(user=auth.get_user(request))
        if employee is not None:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
