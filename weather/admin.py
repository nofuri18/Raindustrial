from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     """Define admin model for custom User model with no username field."""
#     fieldsets = (
#         (None, {'fields': ('nip', 'password')}),
#         (_('Personal info'), {'fields': ('full_name', 'is_active', 'is_staff', 'is_superuser',
#                                        'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('nip', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('nip', 'full_name', 'is_staff')
#     search_fields = ('nip', 'full_name')
#     ordering = ('nip',)

# admin.site.register(get_user_model(), CustomUserAdmin)