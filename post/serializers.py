from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = [
            "author",
            "title",
            "content",
            "created_at",
            "updated_at",
        ]
