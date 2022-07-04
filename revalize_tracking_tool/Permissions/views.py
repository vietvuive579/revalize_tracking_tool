from rest_framework.generics import CreateAPIView ,ListAPIView, RetrieveUpdateDestroyAPIView
from Permissions.models import Role, Permission
from Permissions.serializers import RoleSerializer, PermissionSerializer
from rest_framework.pagination import PageNumberPagination
from Users.permission import IsAdmin

class Pagination(PageNumberPagination):
    page_size = 3

class RoleListAPIView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    pagination_class = Pagination

class RoleCreateAPIView(CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdmin]

class RoleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdmin]



class PermissionListAPIView(ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = Pagination

class PermissionCreateAPIView(CreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAdmin]

class PermissionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAdmin]