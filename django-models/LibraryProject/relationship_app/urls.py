from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import admin_view

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Admin-only view
    path('admin-dashboard/', admin_view, name='admin_dashboard'),

    # Book-related views
    path('books/', views.list_books, name='list_books'),
    path('books/<int:pk>/', views.book_detail_view, name='book_detail'),
]
