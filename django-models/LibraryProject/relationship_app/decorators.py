# relationship_app/decorators.py
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def role_required(role):
    def check_role(user):
        try:
            return user.userprofile.role == role
        except:
            return False
    return user_passes_test(check_role)
