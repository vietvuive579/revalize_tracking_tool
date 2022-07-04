from django.urls import path
from AuthenKeys import views

urlpatterns = [
    path('userlogin/', views.LoginUserAPI.as_view()),
    path('userlogout/', views.LogoutUserAPI.as_view()),
]