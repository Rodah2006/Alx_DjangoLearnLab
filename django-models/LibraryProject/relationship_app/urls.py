from django.urls import path
from . import views
from .views import BookDetailView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.list_books, name='list_books'),  # Home page shows book list

    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),

    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', views.member_view, name='member_dashboard'),
]
