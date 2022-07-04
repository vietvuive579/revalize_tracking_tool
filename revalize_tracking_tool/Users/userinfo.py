from revalize_tracking_tool.enviroment_variable import COOKIE_KEY
from django.conf import settings
import jwt

def get_id_user(request):
    token_encode = request.COOKIES.get(COOKIE_KEY)
    payload = jwt.decode(token_encode, settings.SECRET_KEY)
    user_id = payload['uuid']
    return user_id

def get_token_user(request):
    token_encode = request.COOKIES.get(COOKIE_KEY)
    return token_encode