from django.db import models

import uuid

class BaseInfo(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, null=False)
    friendly_name = models.CharField(max_length=128, null=False)
    code_name = models.CharField(max_length=128, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.UUIDField(uuid.uuid4)
    modified_by = models.UUIDField(uuid.uuid4, null=True)

class Permission(BaseInfo):
    def __str__(self):
        return self.friendly_name

class Role(BaseInfo):
    permisions = models.ManyToManyField(Permission, related_name="roles")

    def __str__(self):
        return self.friendly_name