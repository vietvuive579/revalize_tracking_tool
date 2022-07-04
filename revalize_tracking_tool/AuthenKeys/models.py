from django.db import models
from Users.models import User

class AuthenKey(models.Model):
    token_key = models.CharField(max_length=256, null=False)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user_id.email