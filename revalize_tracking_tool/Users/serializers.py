from Users.models import User
from Permissions.models import Role
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "full_name",
            "phone",
            "created_at",
            "modified_at",
            "roles",
        ]
        extra_kwargs = {
            "password": {'write_only': True},
            "first_name": {'write_only': True},
            "last_name": {'write_only': True},
        }
        read_only_fields = ['full_name', 'created_at', 'modified_at']
        depth = 2

    def create(self, validate_data):
        data = self.context.get('request').data
        new_user = User(**validate_data)
        new_user.password=make_password(validate_data['password'])
        new_user.full_name=validate_data["first_name"] + " " + validate_data["last_name"]
        
        if data.get('roles'):
            for role in data['roles']:
                if not Role.objects.filter(friendly_name=role['friendly_name']).exists():
                    raise serializers.ValidationError('Friendly name is not valid')
                else:
                    new_user.save()
                    role_obj = Role.objects.get(friendly_name=role['friendly_name'])
                    new_user.roles.add(role_obj)
        return new_user

    def validate_phone(self, data):
        if not data.isnumeric():
            raise serializers.ValidationError('Phone number cannot contain characters')
        if len(data) < 9 or len(data) > 12:
            raise serializers.ValidationError('Phone number must be between 9 and 12 digits')
        return data



class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "full_name",
            "phone",
            "created_at",
            "modified_at",
            "roles",
        ]
        extra_kwargs = {
            "first_name": {'write_only': True},
            "last_name": {'write_only': True}
        }
        read_only_fields = ['full_name']
        depth = 2
    
    def update(self, instance, validated_data):
        data = self.context.get('request').data
        method = self.context.get('request').method
        
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.full_name = instance.first_name + " " + instance.last_name
        instance.phone = validated_data.get('phone', instance.phone)
        
        list_id_roles = []     
        if data.get('roles'):
            for value in data['roles']:
                update_role = Role.objects.filter(id=value).first()
                list_id_roles.append(update_role.id)
            if method == "PATCH":
                for value in list_id_roles:
                    instance.roles.add(value)
            else:
                instance.roles.set(list_id_roles)
        instance.save()
        
        return instance

    def validate_phone(self, data):
        if not data.isnumeric():
            raise serializers.ValidationError('Phone number cannot contain characters')
        if len(data) < 9 or len(data) > 12:
            raise serializers.ValidationError('Phone number must be between 9 and 12 digits')
        return data

