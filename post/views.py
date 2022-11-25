from rest_framework.viewsets import ModelViewSet
from .serializers import Postserializer
from .models import Post
# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializer