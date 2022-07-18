from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import MyplantSerializer, PlantsSerializer, PlantsSearchSerializer
from .models import Myplant, Plants
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


User = get_user_model()


# 전체 식물 조회 => 제공하지 않는 기능, 개발 확인용
@api_view(['GET'])
def plants(request):
    plants = get_list_or_404(Plants)
    serializer = PlantsSerializer(plants, many=True)
    return Response(serializer.data)


# 물주기(내 식물) 조회
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def read_myplant(request):
    plants = get_list_or_404(Myplant)

    serializer = MyplantSerializer(plants, many=True)
    return Response(serializer.data)


# 물주기(내 식물) 등록
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_myplant(request, plantname):
    user = request.user
    species = get_object_or_404(Plants, name=plantname)

    serializer = MyplantSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):

        serializer.save(user=user, species=species)

        return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_otp(request, plant_pk):
    plant = get_object_or_404(Plants, pk=plant_pk)
    otp_codes = ''
    
    if plant['otp_code'] == False:
        serializer = MyplantSerializer(instance=plant)
        otp_code = ''
    pass



# 식물 이름 검색
@api_view(['GET'])
def search(request, plantname):
    plants = Plants.objects.filter(name__contains=plantname)
    serializer = PlantsSearchSerializer(plants, many=True)
    return Response(serializer.data)