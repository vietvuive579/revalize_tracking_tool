from rest_framework.generics import CreateAPIView ,ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from TimeTracking.models import Timetracking
from TimeTracking.serializers import TimetrackingSerializer
from TimeTracking.permission import IsMemberTaskOrAdmin


class Pagination(PageNumberPagination):
    page_size = 3


class TimetrackingListAPIView(ListAPIView):
    queryset = Timetracking.objects.all()
    serializer_class = TimetrackingSerializer
    pagination_class = Pagination


class TimetrackingCreateAPIView(CreateAPIView):
    queryset = Timetracking.objects.all()
    serializer_class = TimetrackingSerializer

class TimetrackingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Timetracking.objects.all()
    serializer_class = TimetrackingSerializer