from AuthenKeys.models import AuthenKey
from rest_framework import serializers
from datetime import timedelta
from Users.models import User
from django.contrib.auth.hashers import check_password
from revalize_tracking_tool.enviroment_variable import VALID_HOUR_OF_COOKIE
from django.utils import timezone

class AuthenKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenKey
        fields = '__all__'
        extra_kwargs = {
            "start_date": {'read_only': True},
            "end_date": {'read_only': True}
        }

    def create(self, validate_data):
        request = self.context.get('request')

        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        
        if check_password(password, user.password) == False:
            raise serializers.ValidationError('Incorrect password')
            

        new_authenkey = AuthenKey(**validate_data)
        
        new_authenkey.start_date = timezone.now()
        new_authenkey.end_date = timezone.now() + timedelta(hours=VALID_HOUR_OF_COOKIE)

        new_authenkey.save()
        return new_authenkey
       

      