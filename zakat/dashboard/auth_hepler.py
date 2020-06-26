"""
Module with support logic for auth
"""
from accounts.models import Employee


def check_is_employee(user) -> bool:
    """
    Check is given user has Employee status

    Params:
        user (object): authenticated user

    """
    try:
        Employee.objects.get(user=user)
    except Employee.DoesNotExist:
        return False
    return True
