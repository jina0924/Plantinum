from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    phone_number = models.CharField(max_length=11, blank=True)
    addr = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
    nickname = models.CharField(max_length=15, unique=True)
    photo = models.TextField(blank=True, default='https://url.kr/s38eg6')