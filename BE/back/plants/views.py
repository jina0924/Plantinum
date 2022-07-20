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
    user = request.user
    plants = get_list_or_404(Myplant, user=user)

    serializer = MyplantSerializer(plants, many=True)
    return Response(serializer.data)


# 식물 이름 검색 --> 등록과 합치기
@api_view(['GET'])
def search(request, plantname):
    plants = Plants.objects.filter(name__contains=plantname)
    serializer = PlantsSearchSerializer(plants, many=True)
    return Response(serializer.data)

# 식물 이름 검색을 등록하면서 같이
# 등록할 때 otp 생성
# 5분 카운트걸고 암호 생성 함수 실행
# 물주기(내 식물) 등록 (등록 전 식물 검색 필요)
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

# 커넥티드 안되었는데 otp도 널값이면
# otp 생성
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_otp(request, plant_pk):
    plant = get_object_or_404(Plants, pk=plant_pk)
    otp_codes = ''
    
    if plant['otp_code'] == False:
        serializer = MyplantSerializer(instance=plant)
        otp_code = ''

# 오티피 4자리 유저pk 2자리 식물pk 2자리 랜덤, isconnected로 확인하기



