from django.urls import path
from TimeTracking import views

urlpatterns = [
    path('timetracking_list/', views.TimetrackingListAPIView.as_view()),
    path('create_timetracking/', views.TimetrackingCreateAPIView.as_view()),
    path('timetracking/<uuid:pk>/', views.TimetrackingDetail.as_view())
]