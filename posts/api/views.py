from rest_framework import generics
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsPostAuthorOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

class ListCreatePostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post_author = self.request.user
        serializer.save(post_author=post_author)

class UpdateRetrieveDestroyPostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsPostAuthorOrReadOnly]