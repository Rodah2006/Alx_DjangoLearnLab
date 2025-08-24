from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    CommentViewSet,
    FeedView,
    LikePostView,
    UnlikePostView
)
from django.http import HttpResponse

# Simple home view for root URL
def home(request):
    return HttpResponse("Welcome to the Social Media API!")

# DRF router for posts and comments
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# URL patterns
urlpatterns = [
    # Root URL
    path('', home, name='home'),

    # DRF routes
    path('api/', include(router.urls)),

    # Feed endpoint
    path('feed/', FeedView.as_view(), name='feed'),

    # Like/unlike endpoints
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
