import re
from rest_framework import permissions
from Permissions.models import Role, Permission
from Users.userinfo import get_id_user
from Users.models import User
from TimeTracking.models import Timetracking

        
class IsMemberTaskOrAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # task_of_user = Timetracking.objects.
        print(request)
        print(obj)
        return get_id_user(request) == str(obj.id)
        
