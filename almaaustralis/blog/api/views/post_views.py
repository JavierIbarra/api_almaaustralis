from rest_framework.response import Response
from rest_framework import generics, status

from blog.models import Post
from blog.api.serializers.post_serializers import PostSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer