from rest_framework import serializers
from .models import Plants, Myplant, Sensing
from django.contrib.auth import get_user_model

User = get_user_model()


class MyplantSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'nickname',)

    user = UserSerializer(read_only=True)

    class PlantsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Plants
            fields = ('pk', 'name', 'watercycle_spring_nm', 'watercycle_summer_nm', 'watercycle_autumn_nm', 'watercycle_winter_nm', 'specl_manage_info',)

    name = PlantsSerializer(read_only=True)

    class SensingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Sensing
            fields = '__all__'
    
    sensing = SensingSerializer(read_only=True)
    
    class Meta:
        model = Myplant
        fields = '__all__'


class PlantsSerializer(serializers.ModelSerializer):

    class MyplantSerializer(serializers.ModelSerializer):
        class Meta:
            model = Myplant
            fields = ('pk', 'nickname',)
        
    myplant_set = MyplantSerializer(many=True, read_only=True)

    class Meta:
        model = Plants
        fields = '__all__'


class PlantsSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plants
        fields = ('name',)


class SensingSerializer(serializers.ModelSerializer):

    class MyplantSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Myplant
            fields = ('pk', 'nickname',)

    my_plant = MyplantSerializer(read_only=True)

    class Meta:
        model = Sensing
        fields = '__all__'