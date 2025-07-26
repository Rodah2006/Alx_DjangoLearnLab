from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to display in the user list
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')

    list_filter = ('is_staff', 'is_superuser', 'is_active')

    # Fields shown when editing a user
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    # Fields shown when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)


# Register the CustomUser with the customized admin
admin.site.register(CustomUser, CustomUserAdmin)
