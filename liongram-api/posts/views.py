from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Create your views here.

from rest_framework import generics

from .models import Post
from .serializers import PostBaseModelSerializer, PostListModelSerializer

# 게시글 목록

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

# 게시글 상세

# 게시글 작성

# 게시글 수정1

# 게시글 수정2

# 게시글 삭제

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

class CalculatorAPIView(APIView):
    def get(self, request):
        # 1. 데이터 확인
        num1 = request.GET.get('num1', 0)
        num2 = request.GET.get('num2', 0)
        operators = request.GET.get('operators')

        # 2. 계산
        if operators == '+':
            result = int(num1) + int(num2)
        elif operators == '-':
            result = int(num1) - int(num2)
        elif operators == '*':
            result = int(num1) * int(num2)
        elif operators == '/':
            result = int(num1) / int(num2)
        else:
            result = 0

        data = {
            'type' : 'CBV',
            'result' : result,
        }

        # 응답
        return Response(data)

    def post(self, request):
        data = {
            'type' : 'CBV',
            'method' : 'POST',
            'result' : 0,
        }

        return Response(data)


@api_view()
def calculator(request):
    # 1. 데이터 확인
    num1 = request.GET.get('num1', 0)
    num2 = request.GET.get('num2', 0)
    operators = request.GET.get('operators')

    # 2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    data = {
        'type' : 'FBV',
        'result' : result,
    }

    # 응답
    return Response(data)