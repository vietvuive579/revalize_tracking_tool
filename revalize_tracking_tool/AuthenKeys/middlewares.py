import jwt
from django.utils.deprecation import MiddlewareMixin
from AuthenKeys.models import AuthenKey
from django.conf import settings
from revalize_tracking_tool.enviroment_variable import COOKIE_KEY
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from Users.userinfo import *

class AuthenUser(MiddlewareMixin):    

    def process_request(self, request):
        if request.COOKIES.get(COOKIE_KEY) is not None:
            user_isAuthen = AuthenKey.objects.get(user_id_id=get_id_user(request))
            token_encode = get_token_user(request)
            if user_isAuthen.token_key != token_encode:
                response = Response({"Token is valid, please Login again"}, status=401)
                response.delete_cookie(COOKIE_KEY)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
                return response
            elif not user_isAuthen.start_date <= timezone.now() < user_isAuthen.end_date:
                response = Response({"Time out, please Login again"}, status=401)
                response.delete_cookie(COOKIE_KEY)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
                return response
            else: return
        elif request.path == '/api/register/' or request.path == '/api/userlogout/' or request.path == '/api/userlogin/' or request.path.startswith('/admin'):
            return
        else:
            response = Response({"You not logged in yet"}, status=401)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()
            return response