from django.contrib import admin
from Permissions.models import Permission, Role


admin.site.register(Role)
admin.site.register(Permission)

