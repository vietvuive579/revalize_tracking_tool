from rest_framework.generics import CreateAPIView ,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from AuthenKeys.models import AuthenKey
from rest_framework.response import Response
from AuthenKeys.serializers import AuthenKeySerializer
from Users.models import User
import jwt
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from revalize_tracking_tool.enviroment_variable import *

class LoginUserAPI(CreateAPIView):
    queryset = AuthenKey.objects.all()
    serializer_class = AuthenKeySerializer

    def create(self, request, *args, **kwargs):
        email = request.data['email']

        user = User.objects.filter(email=email).first()

        if user is not None:
            token = self.set_cookie(user)
            dict_data = {
                "token_key": token,
                "user_id": user.id
            }

            serializer = self.get_serializer(data=dict_data)
            if(serializer.is_valid()):
                serializer.save()

            else:
                valid_user = AuthenKey.objects.get(user_id=user.id)
                if dict_data['user_id'] == valid_user.user_id_id:
                    valid_user.token_key = dict_data["token_key"]
                    valid_user.start_date = timezone.now()
                    valid_user.end_date = timezone.now() + timedelta(hours=VALID_HOUR_OF_COOKIE)
                    valid_user.save()

            response = Response(token, status=200)
            response.set_cookie(COOKIE_KEY, token)
            return response

        return Response({"User not found"}, status=400)

    def set_cookie(self, user):
        payload = {
            'uuid': str(user.id),
            'iat': timezone.now()
        }
        token = jwt.encode(payload, settings.SECRET_KEY, 'HS256').decode("utf-8")
        return token


class LogoutUserAPI(APIView):
    def post(self, request):
        #import pdb;pdb.set_trace()
        if request.COOKIES.get(COOKIE_KEY) != None and self.check_cookie(request) == True:
            response = Response({'No content'}, status=204)
            response.delete_cookie(COOKIE_KEY)
            return response
        else: return Response({'You must login first'}, status=400)

    def check_cookie(self, request):
        token_encode = request.COOKIES.get(COOKIE_KEY)
        payload = jwt.decode(token_encode, settings.SECRET_KEY)
        user_isAuthen = AuthenKey.objects.get(user_id_id=payload['uuid'])
        
        if user_isAuthen is not None:
            return True
        return False