from django.shortcuts import redirect
from .models import UserProfile

def role_required(role):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                if user_profile.role == role:
                    return view_func(request, *args, **kwargs)
            except UserProfile.DoesNotExist:
                pass
            return redirect('login')  # or show a permission denied page
        return wrapper
    return decorator
