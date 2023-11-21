from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    age = models.BigIntegerField(null=True)
    phone_number = models.BigIntegerField(null=True)
    Job = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
