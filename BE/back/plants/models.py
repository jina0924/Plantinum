from django.db import models
from django.conf import settings


class Plants(models.Model):
    name = models.CharField(max_length=100)
    hd_code = models.CharField(max_length=6)
    watercycle_spring = models.CharField(max_length=6)
    watercycle_summer = models.CharField(max_length=6)
    watercycle_autumn = models.CharField(max_length=6)
    watercycle_winter = models.CharField(max_length=6)
    specl_manage_info = models.CharField(max_length=100, blank=True, null=True)


class Myplant(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    species = models.ForeignKey(Plants, on_delete=models.PROTECT, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Sensing(models.Model):
    remaining_water = models.BooleanField(default=False)
    state_led = models.BooleanField(default=False)
    moisture_level = models.IntegerField()
    last_watering = models.DateTimeField(auto_now=True)
    my_plant = models.ForeignKey(Myplant, on_delete=models.CASCADE)


class Diary(models.Model):
    content = models.CharField(max_length=1000)
    photo = models.TextField()
    diary_created_at = models.DateTimeField(auto_now_add=True)
    public_private = models.BooleanField(default=False)
    plant = models.ForeignKey(Myplant, on_delete=models.CASCADE)
