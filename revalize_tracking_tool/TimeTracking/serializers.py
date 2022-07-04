from urllib import request
from TimeTracking.models import Timetracking
from rest_framework import serializers
from Users.userinfo import get_id_user

class TimetrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetracking
        fields = '__all__'

    def validate(self, data):
        if data.get('start_time') and data.get('end_time'):
            if data['start_time'] >= data['end_time']:
                raise serializers.ValidationError('End time must be after start time')
        return data

    def create(self, validated_data):
        request = self.context.get('request')
        new_task = Timetracking(**validated_data)
        new_task.created_by = get_id_user(request)

        new_task.save()
        return new_task

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.modified_by = get_id_user(request)
        return super().update(instance, validated_data)