from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Postserializer
from .models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializer

    def dispatch(self, request, *args, **kwargs):
        print("request.body :", request.body)  # 클라이언트의 인코딩에 따라 다른결과를 확인할 수 있다.
        print("request.POST :", request.POST)
        return super().dispatch(request, *args, **kwargs)

    # 해당 요청이 올때마다 실행


class PostListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer

# 하나의 작업만을 구현하고자 할때 @api_view를 쓰면 편리합니다.
@api_view(['GET', 'POST'])
def post_list(request):
    
    if request.method == 'GET':
        serializer = Postserializer(Post.objects.all(), many=True)
        return Response(serializer.data, status=200)
    else:
        serializer = Postserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
