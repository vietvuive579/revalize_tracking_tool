from urllib import request
from Permissions.models import Permission, Role
from rest_framework import serializers, validators
from Users.userinfo import get_id_user

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        exclude=['id', 'created_at', 'modified_at']
        extra_kwargs = {
            "friendly_name": {
                "validators": [
                validators.UniqueValidator(
                    Permission.objects.all(), 'Friendly name already exists.')
                ]
            },
            "created_by": {'read_only': True},
            "modified_by": {'read_only': True}
        }

    def create(self, validate_data):
        user_id = self.context['view'].kwargs.get('user_id')
        
        new_permission = Permission.objects.create(
            friendly_name=validate_data["friendly_name"],
            code_name=validate_data["code_name"],
            created_by=user_id
        )

        new_permission.save()
        return new_permission


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            "friendly_name",
            "code_name",
            "created_at",
            "modified_at",
            "created_by",
            "modified_by",
            "permisions",
        ]
        extra_kwargs = {
            "friendly_name": {
                'validators': [
                validators.UniqueValidator(
                    Role.objects.all(), 'Friendly_namealready exists.')
                ]
            },
            "created_by": {'read_only': True},
            "modified_by": {'read_only': True},
            
        }
        depth = 1

    def create(self, validate_data):
        data = self.context.get('request').data
        request = self.context.get('request')
        
        new_role = Role.objects.create(
            friendly_name=validate_data["friendly_name"],
            code_name=validate_data["code_name"],
            created_by=get_id_user(request)
        )

        for permission in data["permisions"]:
            if not Permission.objects.filter(friendly_name=permission['friendly_name']).exists():
                raise serializers.ValidationError('Friendly name is not valid')
            else:
                new_role.save()
                permission_obj = Permission.objects.get(friendly_name=permission["friendly_name"])
                new_role.permisions.add(permission_obj)

        serializer = RoleSerializer(new_role)

        return serializer.data

    def update(self, instance, validated_data):
        data = self.context.get('request').data
        request = self.context.get('request')

        instance.friendly_name = validated_data.get('friendly_name', instance.friendly_name)
        instance.code_name = validated_data.get('code_name', instance.code_name)
        instance.modified_by = get_id_user(request)
        
        list_permissions = []
        for value in data['permisions']:
            if value.get('friendly_name'):
                update_permission = Role.objects.filter(friendly_name=value.get('friendly_name')).first()
                if(update_permission == None):
                    raise serializers.ValidationError('Incorrect Friendly name')
                list_permissions.append(update_permission)
            else: raise serializers.ValidationError('Friendly name is not choose')  

        instance.permisions.set(list_permissions)
        instance.save()

        return instance