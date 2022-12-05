from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({
            'post': PostSerializer(post).data
        })