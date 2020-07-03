from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

from accounts.models import Employee


class EmployeePermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if Employee.objects.get(user=request.user):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
