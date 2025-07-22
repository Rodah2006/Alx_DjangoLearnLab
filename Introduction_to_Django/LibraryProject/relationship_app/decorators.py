from django.http import HttpResponseForbidden

def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and hasattr(request.user, 'profile') and request.user.profile.role == role:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You are not authorized to view this page.")
        return _wrapped_view
    return decorator
