from django.http import HttpResponseForbidden
from functools import wraps

def role_required(role_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("You are not allowed to view this page.")

            if hasattr(request.user, 'role') and request.user.role == role_name:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Access denied: Admins only.")
        return _wrapped_view
    return decorator
