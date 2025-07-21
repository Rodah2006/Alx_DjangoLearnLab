from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
