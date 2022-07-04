from django.urls import path
from Users import views

urlpatterns = [
    path('user/', views.UserlistAPIView.as_view()),
    path('user/<uuid:pk>', views.UserDetailAPIView.as_view()),
    path('register/', views.UserCreateAPIView.as_view())
]