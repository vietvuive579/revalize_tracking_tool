from django.urls import path
from Permissions import views

urlpatterns = [
    path('role_list/', views.RoleListAPIView.as_view()),
    path('create_role/', views.RoleCreateAPIView.as_view()),
    path('role_detail/<uuid:pk>/', views.RoleDetail.as_view()),

    path('permission_list/', views.PermissionListAPIView.as_view()),
    path('create_permission/', views.PermissionCreateAPIView.as_view()),
    path('permission_detail/<uuid:pk>/', views.PermissionDetail.as_view()),
]