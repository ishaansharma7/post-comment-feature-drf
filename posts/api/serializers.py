from rest_framework import serializers
from posts.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    post_author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    original_post = serializers.StringRelatedField(read_only=True)
    comment_author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'