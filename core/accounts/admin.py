from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ('email',)
    list_display = (
        'email','is_active', 'is_superuser', 'last_login', 'is_verified'
    )
    list_filter = (
        'is_active', 'is_superuser', 'is_verified', 'is_staff'
        
    )
    fieldsets = (
        ('Authentication', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Group Permissions', {'fields':('groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )


admin.site.register(Profile)