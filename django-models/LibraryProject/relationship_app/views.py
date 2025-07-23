from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import UserProfile, Library, Book  # ✅ Include your models here


# 🌐 Home page for all logged-in users
@login_required
def home(request):
    return render(request, 'relationship_app/home.html')


# 🔐 Admin view — only accessible if role is Admin
@login_required
def admin_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Admin':
            libraries = Library.objects.all()  # Example: display all libraries
            return render(request, 'relationship_app/admin.html', {'libraries': libraries})
        else:
            return HttpResponseForbidden("You are not authorized to access this page.")
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("User profile not found.")


# 📚 Librarian view — only accessible if role is Librarian
@login_required
def librarian_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Librarian':
            books = Book.objects.all()  # Example: display all books
            return render(request, 'relationship_app/librarian.html', {'books': books})
        else:
            return HttpResponseForbidden("You are not authorized to access this page.")
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("User profile not found.")


# 🙋 Member view — only accessible if role is Member
@login_required
def member_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Member':
            books = Book.objects.all()  # You can customize what members can see
            return render(request, 'relationship_app/member.html', {'books': books})
        else:
            return HttpResponseForbidden("You are not authorized to access this page.")
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("User profile not found.")
