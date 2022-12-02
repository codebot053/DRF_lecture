from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    '''
    postlist, postdetail 의 기능 CRRUD를 담당합니다.
    list, create => /post/
    detail(retrieve), update, Destroy => /post/<int:pk>/
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs):
        print("request.body :", request.body)  # 클라이언트의 인코딩에 따라 다른결과를 확인할 수 있다.
        print("request.POST :", request.POST)
        return super().dispatch(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        '''
        해당 유저정보를 form, json을 통하지 않고 request 통해 저장
        '''
        serializer.save(author=self.request.user)
