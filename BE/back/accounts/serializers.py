from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):

    phone_number = serializers.CharField(max_length=11)
    addr = serializers.CharField(max_length=100)
    zip_code = serializers.IntegerField()
    nickname = serializers.CharField(max_length=15)
    email = serializers.EmailField()


    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['phone_number'] = self._validated_data.get('phone_number', '')
        data['addr'] = self._validated_data.get('addr', '')
        data['zip_code'] = self._validated_data.get('zip_code', '')
        data['nickname'] = self._validated_data.get('nickname', '')
        data['email'] = self._validated_data.get('email', '')
        return data