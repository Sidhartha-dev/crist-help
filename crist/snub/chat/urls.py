from django.urls import path
from . import apis
from .apis import  UserList, MyTokenObtainPairView, currUser, PostList
from .views import index
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("",index, name="index"),
    path('posts/', PostList.as_view()),
    path('posts/<int:id>/', PostList.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:id>', UserList.as_view()),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('me/', currUser.as_view()),
    path('userposts/', apis.authUserPosts),
]