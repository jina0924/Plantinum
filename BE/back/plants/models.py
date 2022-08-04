from django.db import models
from django.conf import settings


class Plants(models.Model):
    name = models.CharField(max_length=100)
    watercycle_spring = models.CharField(max_length=6)
    watercycle_spring_nm = models.CharField(max_length=30)
    watercycle_summer = models.CharField(max_length=6)
    watercycle_summer_nm = models.CharField(max_length=30)
    watercycle_autumn = models.CharField(max_length=6)
    watercycle_autumn_nm = models.CharField(max_length=30)
    watercycle_winter = models.CharField(max_length=6)
    watercycle_winter_nm = models.CharField(max_length=30)
    specl_manage_info = models.TextField(blank=True)


class Myplant(models.Model):
    nickname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    otp_code = models.CharField(max_length=6, unique=True, null=True)
    plant_info = models.ForeignKey(Plants, on_delete=models.PROTECT, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # photo = models.ImageField(upload_to='images/', blank=True)
    photo = models.TextField(blank=True, default='https://url.kr/d1acln')
    is_connected = models.BooleanField(default=False)

from annoying.fields import AutoOneToOneField

class Sensing(models.Model):
    remaining_water = models.BooleanField(default=False)
    state_led = models.BooleanField(default=False)
    moisture_level = models.IntegerField(default=0)
    last_watering = models.CharField(max_length=16, blank=True)
    # my_plant = models.OneToOneField(Myplant, on_delete=models.CASCADE)
    my_plant = AutoOneToOneField(Myplant, on_delete=models.CASCADE)


class Diary(models.Model):
    content = models.CharField(max_length=1000)
    photo = models.TextField(blank=True, default='https://url.kr/d1acln')
    diary_created_at = models.DateTimeField(auto_now_add=True)
    public_private = models.BooleanField(default=False)
    my_plant = models.ForeignKey(Myplant, on_delete=models.CASCADE)
