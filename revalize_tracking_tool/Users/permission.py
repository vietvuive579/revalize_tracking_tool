from rest_framework import permissions
from Permissions.models import Role, Permission
from Users.userinfo import get_id_user

class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        queryset = Role.objects.prefetch_related('users')
        try:
            user_role = queryset.get(users=get_id_user(request), friendly_name='Admin')
            user_permission = Permission.objects.get(roles=user_role.id)
            if user_permission.code_name == "all":
                return True
        except: pass
        
class IsMemberOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return get_id_user(request) == str(obj.id)
        
