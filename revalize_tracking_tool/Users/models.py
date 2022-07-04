from django.db import models
import uuid
from Permissions.models import Role

# Create your models here.
class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    first_name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null=False)
    full_name = models.CharField(max_length=128, null=False)
    phone = models.CharField(max_length=128, null=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    roles = models.ManyToManyField(Role, related_name="users")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'