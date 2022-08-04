from django.shortcuts import get_object_or_404
from .serializers import JusoSidoSerializer, JusoSigunguSerializer, Leaf82Serializer, Leaf82ListSerializer
from .models import Juso, Leaf82
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
import random


User = get_user_model()


# 잎팔이 글 작성
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_leaf82(request):
    sido = request.data['sido']
    sigungu = request.data['sigungu']
    addr = get_object_or_404(Juso, sido=sido, sigungu=sigungu)
    user = request.user
    posting_addr = 0

    while posting_addr == 0:
        posting_addr = random.randint(100000, 999999)
        if Leaf82.objects.filter(user=user, posting_addr=posting_addr).exists():  # 중복체크, 한 유저 내에서 중복x
            posting_addr = 0

    serializer = Leaf82Serializer(data=request.data)
        
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, addr=addr, posting_addr=posting_addr)
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
    serializer = Leaf82ListSerializer(leaves, many=True)
    return Response(serializer.data)


# # 잎팔이 특정 지역/동네 글 조회  => 제공 x
# @api_view(['GET'])
# def sido_sigungu_leaf82(request, sido, sigungu):

#     sido_sigungu = Juso.objects.filter(sido=sido, sigungu__contains=sigungu)
    
#     leaves = Leaf82.objects.filter(addr__in=sido_sigungu).order_by('-pk')
#     serializer = Leaf82Serializer(leaves, many=True)
#     return Response(serializer.data)


# from rest_framework.views import APIView
# class Leaf82View(APIView):
#     def get(self, request):
#         plantname = request.GET.get('plantname', '*')

#         return Response({'result': '111111'})

@api_view(['GET'])
def search(request):
    # 식물이름(검색어)/시도/시군구

    plantname = request.GET.get('plantname', '*')
    sido = request.GET.get('sido', '*')
    sigungu = request.GET.get('sigungu', '*')

    leaves = Leaf82.objects.filter().order_by('-pk')
    if plantname != '*':
        leaves = leaves.filter(plantname__contains=plantname)
        
    if sido != '*':
        addr1 = Juso.objects.filter(sido=sido)
        leaves = leaves.filter(addr__in=addr1)

    if sigungu != '*':
        addr2 = Juso.objects.filter(sigungu__contains=sigungu)
        leaves = leaves.filter(addr__in=addr2)

    serializer = Leaf82ListSerializer(leaves, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request, username, posting_addr):
    user = User.objects.filter(username=username)[0]
    
    leaf82 = get_object_or_404(Leaf82, user=user, posting_addr=posting_addr)

    serializer = Leaf82Serializer(leaf82)
    return Response(serializer.data)