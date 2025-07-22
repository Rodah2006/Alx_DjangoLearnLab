from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('books/', views.list_books, name='list_books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),

    # Step 4: Add role-based dashboard URLs
    path('admin_page/', views.admin_page, name='admin_page'),
    path('librarian_page/', views.librarian_page, name='librarian_page'),
    path('member_page/', views.member_page, name='member_page'),
]
