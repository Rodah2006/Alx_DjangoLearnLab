from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Example of linking to book views
    path('books/', views.list_books, name='list_books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]
