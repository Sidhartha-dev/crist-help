from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializers, UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class PostList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    # permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class UserList(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    # def post(self, request):
    #     return self.create(request)

    # def put(self, request, id=None):
    #     return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)




class currUser(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def authUserPosts(request):
    user = request.user
    posts = user.author.all()
    serializer = PostSerializers(posts, many=True, context={'request': request})
    return Response(serializer.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=200)
    # else:
    #     return Response(serializer.errors, status=400)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer