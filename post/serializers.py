from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class AuthorSerializer(serializers.ModelSerializer):
    # Post 모델의 fk author을 중첩된 serializer를 통해서 구현
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]


class Postserializer(serializers.ModelSerializer):
    # username = serializers.ReadOnlyField(source='author.username')
    # post 모델에서 fk 로 참조하는 user의 username을 읽을수 있다. CASE 1
    author = AuthorSerializer()
    # serializer 중첩
    class Meta:
        model = Post
        fields = [
            "pk",
            "author",
            "title",
            "content",
            "created_at",
            "updated_at",
        ]
