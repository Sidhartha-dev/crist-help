from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
class PostSerializers(serializers.ModelSerializer):
    # img_url = serializers.SerializerMethodField('get_photo_url')
    class Meta:
        model= Post
        fields= ('title', 'post_date', 'author', 'photo')
    # def get_photo_url(self, obj):
    #     return obj.photo.url

class UserSerializer(serializers.ModelSerializer):
    author = PostSerializers(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'author']