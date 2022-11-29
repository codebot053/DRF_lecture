from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
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
