from rest_framework import serializers
# from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import User

# class CustomRegisterSerializer(RegisterSerializer):

#     phone_number = serializers.CharField(max_length=11)
#     addr = serializers.CharField(max_length=100)
#     zip_code = serializers.CharField(max_length=5)
#     nickname = serializers.CharField(max_length=15)


#     def get_cleaned_data(self):
#         data = super().get_cleaned_data()
#         data['phone_number'] = self._validated_data.get('phone_number', '')
#         data['addr'] = self._validated_data.get('addr', '')
#         data['zip_code'] = self._validated_data.get('zip_code', '')
#         data['nickname'] = self._validated_data.get('nickname', '')
#         return data

