from django.contrib.auth.models import AbstractUser
from django.db import models
# import random


class User(AbstractUser):

    # full_nickname = ''

    # while full_nickname == '':
    #     nick1_lst = ['촉촉한', '싱싱한', '늘푸른', '건강한', '새내기']
    #     nick2_lst = ['참나무', '소나무', '올리브나무', '야자나무', '귤나무']
    #     nick1 = random.choice(nick1_lst)
    #     nick2 = random.choice(nick2_lst)
    #     nick3 = str(random.randint(0, 9999))
    
    #     full_nickname = nick1+nick2+nick3

    #     if User.objects.filter(nickname=full_nickname).exists():
    #         full_nickname = ''
    
    phone_number = models.CharField(max_length=11, blank=True)
    addr = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
    nickname = models.CharField(max_length=15, unique=True)
    