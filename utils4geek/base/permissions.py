from rest_framework.permissions import BasePermission
from rest_framework.compat import is_authenticated


class IsUserActive(BasePermission):
    """
    Allows access only to authenticated users.
    """
    message = 'Your account has been disabled.'

    def has_permission(self, request, view):
        return request.user.is_active