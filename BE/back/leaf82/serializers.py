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

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'nickname',)

    user = UserSerializer(read_only=True)

    class JusoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Juso
            fields = '__all__'

    addr = JusoSerializer(read_only=True)

    class Meta:
        model = Leaf82
        fields = '__all__'