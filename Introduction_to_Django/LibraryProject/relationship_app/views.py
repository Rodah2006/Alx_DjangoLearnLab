# LibraryProject/relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # or any page you'd like after login
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .decorators import role_required

@login_required
@role_required('Admin')  # Only users with role == 'Admin' allowed
def admin_view(request):
    return render(request, 'relationship_app/admin.html')

@login_required
def librarian_page(request):
    return render(request, 'relationship_app/librarian_page.html')

@login_required
def member_page(request):
    return render(request, 'relationship_app/member_page.html')
