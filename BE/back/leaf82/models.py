from django.db import models
from django.conf import settings


class Leaf82(models.Model):
    plantname = models.CharField(max_length=100)
    photo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000)
    price = models.IntegerField()
    status_class = models.CharField(max_length=5)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    addr_si = models.CharField(max_length=1)
    addr_gungu = models.CharField(max_length=1)