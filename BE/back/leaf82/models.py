from django.db import models
from django.conf import settings


class Juso(models.Model):
    sido = models.CharField(max_length=20)
    sigungu = models.CharField(max_length=20)


class Leaf82(models.Model):
    CATEGORY_CHOICES = (
        ('분양해요', '분양해요'),
        ('분양받아요', '분양받아요')
    )
    STATUS_CHOICES = (
        ('판매중', '판매중'),
        ('거래완료', '거래완료'),
        ('예약중', '예약중')
    )

    plantname = models.CharField(max_length=100)
    photo = models.TextField(blank=True, default='https://url.kr/d1acln')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000)
    price = models.IntegerField()
    category_class = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    status_class = models.CharField(max_length=4, choices=STATUS_CHOICES, default='판매중')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    addr = models.ForeignKey(Juso, on_delete=models.PROTECT)
    posting_addr = models.IntegerField(default=0)