from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import MyplantSerializer, PlantsSerializer, PlantsSearchSerializer, DiarySerializer, MyplantListSerializer
from .models import Myplant, Plants, Diary
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


User = get_user_model()


# 전체 식물 조회 => 제공하지 않는 기능, 개발 확인용
@api_view(['GET'])
def plants(request):
    plants = get_list_or_404(Plants)
    serializer = PlantsSerializer(plants, many=True)
    return Response(serializer.data)


# 내 식물 전체 조회 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def read_myplant(request, usernickname):
    user = get_object_or_404(User, nickname=usernickname)
    plants = get_list_or_404(Myplant, user=user)

    serializer = MyplantListSerializer(plants, many=True)
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


# 물주기(내 식물) 등록 (등록 전 식물 검색 필요)
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_myplant(request):
    
    user = request.user

    otp_code = ''

    # while otp_code == '':

    #     otp_code = random.randint(0, 9999)
    #     otp_code = str(otp_code).zfill(4)

    #     # print(otp_code)

    #     if Myplant.objects.filter(otp_code=otp_code).exists():  # db 존재 여부 확인
    #         otp_code = ''  # 재발급

    serializer = MyplantSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        name_id = request.data['name_id']
        if Plants.objects.filter(pk=name_id).exists():
            name = Plants.objects.get(pk=name_id)
            
            serializer.save(user=user, name=name, otp_code=otp_code)
        else:
            serializer.save(user=user, otp_code=otp_code)

        # def otp():

        #     myplant = Myplant.objects.filter(pk=serializer.data['id'])
        #     # print(myplant.values('otp_code'))  otp code 존재
        #     myplant.update(otp_code='')
        #     # print(myplant.values('otp_code'))  otp code 삭제

        # Timer(301, otp).start()  # 5분 뒤 함수 실행

        return Response(serializer.data)


# 연결되지 않은 상태, otp도 없는 상태에서 otp 발급
# 5분이 지나면 otp 삭제
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_otp(request, myplant_pk):
    if Myplant.objects.filter(pk=myplant_pk, otp_code='', is_connected=False).exists():

        otp_code = ''

        while otp_code == '':

            otp_code = random.randint(0, 999999)
            otp_code = str(otp_code).zfill(6)

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
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def disconnect(request, myplant_pk):
    if Myplant.objects.filter(pk=myplant_pk, is_connected=True).exists():
        myplant = Myplant.objects.filter(pk=myplant_pk, is_connected=True)
        myplant.update(is_connected=False)

        return Response({'is_connected': False})

    else:
        return Response({'result': '연결상태를 확인해주세요.'})


# 물주기 식물 상세페이지
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detail(request, myplant_pk):
    myplant = get_object_or_404(Myplant, pk=myplant_pk)
    serializer = MyplantSerializer(myplant)
    return Response(serializer.data)


# 물주기 각 식물 별 다이어리-식물 별 전체조회/다이어리 작성
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def diary(request, myplant_pk):

    def read_diary():
        diary = get_list_or_404(Diary, my_plant_id=myplant_pk)
        serializer = DiarySerializer(diary, many=True)
        return Response(serializer.data)

    def create_diary():
        my_plant = get_object_or_404(Myplant, pk=myplant_pk)
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(my_plant=my_plant)
            return Response(serializer.data)

    if request.method == 'GET':
        return read_diary()
    elif request.method == 'POST':
        return create_diary()
    # 삭제 추가하기

