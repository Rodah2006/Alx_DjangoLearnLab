from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, RegisterView

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Auth URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
