from django.db import models
from django.conf import settings


class Plants(models.Model):
    name = models.CharField(max_length=100)
    watercycle_spring = models.CharField(max_length=6)
    watercycle_spring_nm = models.CharField(max_length=100)
    watercycle_summer = models.CharField(max_length=6)
    watercycle_summer_nm = models.CharField(max_length=100)
    watercycle_autumn = models.CharField(max_length=6)
    watercycle_autumn_nm = models.CharField(max_length=100)
    watercycle_winter = models.CharField(max_length=6)
    watercycle_winter_nm = models.CharField(max_length=100)
    specl_manage_info = models.TextField(blank=True)


class Myplant(models.Model):
    nickname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    otp_code = models.CharField(max_length=6, blank=True)
    name = models.ForeignKey(Plants, on_delete=models.PROTECT, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # photo = models.ImageField(upload_to='images/', blank=True)
    photo = models.TextField(blank=True)
    is_connected = models.BooleanField(default=False)


class Sensing(models.Model):
    remaining_water = models.BooleanField(default=False)
    state_led = models.BooleanField(default=False)
    moisture_level = models.IntegerField()
    last_watering = models.DateTimeField(auto_now=True)
    my_plant = models.ForeignKey(Myplant, on_delete=models.CASCADE)


class Diary(models.Model):
    content = models.CharField(max_length=1000)
    photo = models.TextField(blank=True)
    diary_created_at = models.DateTimeField(auto_now_add=True)
    public_private = models.BooleanField(default=False)
    my_plant = models.ForeignKey(Myplant, on_delete=models.CASCADE)

