from Users.models import User
from Users.serializers import UserSerializer, UserUpdateSerializer
from rest_framework.generics import CreateAPIView ,ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from .permission import IsAdmin, IsMemberOwner

class UserPagination(PageNumberPagination):
    page_size = 5

class UserlistAPIView(ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    permission_classes = [IsAdmin]


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsMemberOwner]

