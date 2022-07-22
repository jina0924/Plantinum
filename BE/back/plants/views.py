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


# 식물 이름 검색
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search(request, plantname):
    plants = Plants.objects.filter(name__contains=plantname)
    serializer = PlantsSearchSerializer(plants, many=True)
    return Response(serializer.data)


from threading import Timer
import random


# 등록할 때 5분 카운트걸고 암호 생성 함수 실행, 시간이 지나면 db에서 암호 삭제
# 물주기(내 식물) 등록 (등록 전 식물 검색 필요)
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_myplant(request, plantname):
    
    user = request.user

    otp_code = ''

    while otp_code == '':

        otp_code = random.randint(0, 9999)
        otp_code = str(otp_code).zfill(4)

        # print(otp_code)

        if Myplant.objects.filter(otp_code=otp_code).exists():  # db 존재 여부 확인
            otp_code = ''  # 재발급

    serializer = MyplantSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):

        if Plants.objects.filter(name=plantname).exists():
            name = Plants.objects.get(name=plantname)
            serializer.save(user=user, name=name, otp_code=otp_code)
        else:
            serializer.save(user=user, otp_code=otp_code)

        def otp():

            myplant = Myplant.objects.filter(pk=serializer.data['id'])
            # print(myplant.values('otp_code'))  otp code 존재
            myplant.update(otp_code='')
            # print(myplant.values('otp_code'))  otp code 삭제

        Timer(301, otp).start()  # 5분 뒤 함수 실행

        return Response(serializer.data)


# 연결되지 않은 상태, otp도 없는 상태에서 otp 발급
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_otp(request, myplant_pk):
    if Myplant.objects.filter(pk=myplant_pk, otp_code='', is_connected=False).exists():

        otp_code = ''

        while otp_code == '':

            otp_code = random.randint(0, 9999)
            otp_code = str(otp_code).zfill(4)

            # print(otp_code)

            if Myplant.objects.filter(otp_code=otp_code).exists():  # db 존재 여부 확인
                otp_code = ''  # 재발급

        myplant = Myplant.objects.filter(pk=myplant_pk)
        myplant.update(otp_code=otp_code)

        # myplant_s = get_object_or_404(Myplant, pk=myplant_pk)
        # serializer = MyplantSerializer(myplant_s)

        def delete_otp():
            myplant.update(otp_code='')
        Timer(301, delete_otp).start()  # 5분뒤 삭제 함수 실행

        # return Response(serializer.data)
        return Response({'otp_code': otp_code})

    else:
        return Response({'result': '이미 발급되었거나 연결되었습니다.'})


# 연결끊기
# 물주기 식물 상세페이지