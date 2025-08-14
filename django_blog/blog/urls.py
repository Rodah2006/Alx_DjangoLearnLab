from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    register,
    profile,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    # Blog post CRUD URLs
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Authentication URLs
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),

    # Comment URLs (FBVs)
    path('post/<int:post_id>/comments/new/', views.add_comment, name='add-comment'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit-comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete-comment'),

# Comment URLs (CBVs)
path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit-comment'),
path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
