from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import PostSerializer
from .models import Post

class PostDetailAPIView(RetrieveAPIView):
    '''
    특정 요청(Retrieve)에 대해서 HTML로 render하여 응답할 경우
    '''
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    # Response에서 kwargs 로 넘겨도 된다.
    template_name = 'post/post_detail.html'
    
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({
            'post': PostSerializer(post).data
        })