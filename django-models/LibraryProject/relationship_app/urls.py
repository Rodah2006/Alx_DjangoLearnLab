from django.urls import path
from . import views

urlpatterns = [
    path('library/<int:pk>/', views.library_detail, name='library_detail'),
]
