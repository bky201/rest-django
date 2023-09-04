from django.urls import path
from posts.views import PostList

urlpatterns = [
    path('posts/', PostList.as_view()),
]