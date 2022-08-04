from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from pytz import utc
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import MyProfileSerializer, UpdateUserInformationSerializer
import datetime


User = get_user_model()


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serializer = MyProfileSerializer(user)
    
    pk = user.pk
    nickname = user.nickname
    email = user.email
    phone_number = user.phone_number
    addr = user.addr
    zip_code = user.zip_code
    myplant_count = serializer.data.get('myplant_count')
    date_joined = user.date_joined
    today = datetime.datetime.now(tz=utc)
    # today = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    dday = (today - date_joined).days+1
    photo = user.photo

    data = {
        'pk': pk,
        'nickname': nickname,
        'email': email,
        'phone_number': phone_number,
        'addr': addr,
        'zip_code': zip_code,
        'myplant_count': myplant_count,
        'dday': dday,
        'photo': photo
    }
    
    return Response(data)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateuserinformation(request):
    user = request.user
    myplant_count = UpdateUserInformationSerializer(user).data.get('myplant_count')
    serializer = UpdateUserInformationSerializer(instance=user, data=request.data)
    date_joined = user.date_joined
    today = datetime.datetime.now(tz=utc)
    # today = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    dday = (today - date_joined).days+1
    
    new_email = request.data['email']
    new_nickname = request.data['nickname']

    if User.objects.filter(email=new_email).exists():
        email_user = User.objects.filter(email=new_email)[0]
    if User.objects.filter(nickname=new_nickname).exists():
        nickname_user = User.objects.filter(nickname=new_nickname)[0]


    # 이메일과 닉네임 모두 이미 존재하는 경우
    if User.objects.filter(email=new_email).exists() and User.objects.filter(nickname=new_nickname).exists():

        # 이메일과 닉네임 모두 유저의 기존 값과 다른 경우
        if email_user != user and nickname_user != user:
            return Response({
                'email': '이메일잘못됨',
                'nickname': '닉네임 잘못됨'
                })

        # 이메일은 유저의 기존 값과 동일, 닉네임은 유저의 기존 값과 다른 경우
        if email_user == user and nickname_user != user:
            return Response({
            'nickname': '닉네임 잘못됨'
            })

        # 이메일은 유저의 기존 값과 다르고, 닉네임은 유저의 기존 값과 동일한 경우
        if email_user != user and nickname_user == user:
            return Response({
            'email': '이메일잘못됨',
            })

        # 이메일과 닉네임 모두 유저의 기존 값과 같은 경우 - 그대로 저장
        if email_user == user and nickname_user == user:
            if serializer.is_valid(raise_exception=True):
                serializer.save(myplant_count=myplant_count, dday=dday)
                return Response(serializer.data)

    # 이메일이 이미 존재하는 경우
    if User.objects.filter(email=new_email).exists():

        # 이메일이 유저의 기존 값과 다른 경우
        if email_user != user:
            return Response({
                'email': '이메일잘못됨',
                })

        # 이메일이 유저의 기존 값과 같은 경우
        if email_user == user:
            if serializer.is_valid(raise_exception=True):
                serializer.save(myplant_count=myplant_count, dday=dday)
                return Response(serializer.data)

    # 닉네임이 이미 존재하는 경우
    if User.objects.filter(nickname=request.data['nickname']).exists():

        # 닉네임이 유저의 기존 값과 다른 경우
        if nickname_user != user:
            return Response({
                'nickname': '닉네임 잘못됨'
                })

        # 닉네임이 유저의 기존 값과 같은 경우
        if nickname_user == user:
            if serializer.is_valid(raise_exception=True):
                serializer.save(myplant_count=myplant_count, dday=dday)
                return Response(serializer.data)

    # 그 외 유효성검사에 걸리는 경우
    if serializer.is_valid(raise_exception=True):
        
        serializer.save(myplant_count=myplant_count, dday=dday)
        return Response(serializer.data)

