# relationship_app/decorators.py
from django.http import HttpResponseForbidden

def role_required(required_role):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if hasattr(request.user, 'userprofile') and request.user.userprofile.role == required_role:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("Access denied: You don't have the required role.")
        return wrapper
