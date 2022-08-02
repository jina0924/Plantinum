from rest_framework import serializers
from .models import Juso, Leaf82
from django.contrib.auth import get_user_model


User = get_user_model()


class JusoSidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Juso
        fields = ('pk', 'sido',)


class JusoSigunguSerializer(serializers.ModelSerializer):

    class Meta:
        model = Juso
        fields = ('pk', 'sigungu',)


class Leaf82Serializer(serializers.ModelSerializer):

    class Meta:
        model = Leaf82
        fields = '__all__'