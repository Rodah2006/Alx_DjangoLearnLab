from django.urls import path
from .views import register_view, login_view, logout_view, BookDetailView, list_books

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('books/', list_books, name='list_books'),  # view all books
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # single book detail
]
