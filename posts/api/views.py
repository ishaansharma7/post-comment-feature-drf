from rest_framework import generics, status
from rest_framework.response import Response
from posts.models import Post, Comment
from posts.api.serializers import PostSerializer, CommentSerializer
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

class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        comment_author = self.request.user
        original_post_pk = self.kwargs.get('pk')
        original_post = Post.objects.get(pk=original_post_pk)
        serializer.save(original_post=original_post, comment_author=comment_author)

class PostCommentsView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def list(self, request, *args, **kwargs):
        original_post = self.kwargs.get('pk')
        post_comments = Comment.objects.filter(original_post=original_post)
        serializer = self.serializer_class(post_comments, many=True)
        return Response(serializer.data)

class UpdateRetrieveDestroyCommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsPostAuthorOrReadOnly]