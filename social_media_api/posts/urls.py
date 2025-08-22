from django.urls import path
from django.http import JsonResponse

def placeholder_view(request):
    return JsonResponse({"message": "Posts app is working!"})

urlpatterns = [
    path('', placeholder_view, name='posts-home'),
]

from django.urls import path
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]
