from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    addr = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    nickname = models.CharField(max_length=15, unique=True)
    