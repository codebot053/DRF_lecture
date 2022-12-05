from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, action
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

    @action(detail=False, methods=['GET'])
    def public(self, request):
        '''
        is_public 필드값이 True인 글들만 리스트 합니다.
        '''
        qs = self.queryset.filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        '''
        is_public 필드값을 True 로 변경 합니다.
        '''
        instance = self.get_object()
        public_status = instance.is_public
        if public_status:
            public_status = False
        else:
            public_status = True
        instance.is_public = public_status
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def dispatch(self, request, *args, **kwargs):
        print("request.body :", request.body)  # 클라이언트의 인코딩에 따라 다른결과를 확인할 수 있다.
        print("request.POST :", request.POST)
        return super().dispatch(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        '''
        해당 유저정보를 form, json을 통하지 않고 request 통해 저장
        '''
        serializer.save(author=self.request.user)
