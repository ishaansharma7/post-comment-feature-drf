from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    post_author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'