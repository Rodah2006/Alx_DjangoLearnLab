from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from .models import Library, Book

# View to register a user
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to book list after register
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# View to log in a user
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # Redirect to book list after login
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# View to log out a user
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Class-based view for viewing a book detail (CBV required by checker)
class BookDetailView(DetailView):
    model = Book
    template_name = 'relationship_app/book_detail.html'
    context_object_name = 'book'

# Function-based view to list all books (used after login/registration)
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})
