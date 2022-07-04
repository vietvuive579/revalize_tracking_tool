from django.db import models
from Users.models import User
import uuid

class Timetracking(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, null=False)
    user_id = models.ForeignKey(User, related_name="timetracking", null=False, on_delete=models.CASCADE)
    release = models.CharField(max_length=128, null=False)
    task_id = models.CharField(max_length=128, null=False)
    task_link = models.CharField(max_length=128)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=128, null=False)
    note = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.UUIDField(uuid.uuid4, null=True)
    modified_by = models.UUIDField(uuid.uuid4, null=True)

    def __str__(self):
        return f'{self.user_id} {self.task_id}'
