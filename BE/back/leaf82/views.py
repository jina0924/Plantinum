from django.shortcuts import get_object_or_404
from .serializers import JusoSidoSerializer, JusoSigunguSerializer, Leaf82Serializer
from .models import Juso, Leaf82
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# 잎팔이 글 작성
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_leaf82(request):
    sido = request.data['sido']
    sigungu = request.data['sigungu']
    addr = get_object_or_404(Juso, sido=sido, sigungu=sigungu)

    user = request.user

    serializer = Leaf82Serializer(data=request.data)
        
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, addr=addr)
        return Response(serializer.data)


# 시도(지역) 검색
@api_view(['GET'])
def search_sido(request):
    data = Juso.objects.all()
    sido = []
    for s in data:
        sido_name = {
            "sido": s.sido
        }

        if sido and sido[-1] == sido_name:
            continue
        sido.append(sido_name)

    return Response(sido)


# 시군구(동네) 검색
@api_view(['GET'])
def search_sigungu(request, sido):
    sigungu = Juso.objects.filter(sido=sido)
    serializer = JusoSigunguSerializer(sigungu, many=True)
    return Response(serializer.data)


# 잎팔이 전체 글 조회 (지역 상관 X)
@api_view(['GET'])
def read_leaf82(request):

    leaves = Leaf82.objects.all().order_by('-pk')
    serializer = Leaf82Serializer(leaves, many=True)
    return Response(serializer.data)


# 잎팔이 특정 지역/동네 글 조회
@api_view(['GET'])
def sido_sigungu_leaf82(request, sido, sigungu):

    sido_sigungu = Juso.objects.filter(sido=sido, sigungu__contains=sigungu)
    
    leaves = Leaf82.objects.filter(addr__in=sido_sigungu).order_by('-pk')
    serializer = Leaf82Serializer(leaves, many=True)
    return Response(serializer.data)


# from rest_framework import generics
# from django_filters import rest_framework as filters
# @api_view(['GET'])
# def search_neighborhood(request):
    