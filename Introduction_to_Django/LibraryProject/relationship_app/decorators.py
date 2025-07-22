from functools import wraps
from django.shortcuts import redirect

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and hasattr(request.user, 'role') and request.user.role == role:
                return view_func(request, *args, **kwargs)
            return redirect('login')  # or 'permission_denied'
        return _wrapped_view
    return decorator
