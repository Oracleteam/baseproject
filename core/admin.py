from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Department, Menu, Userinfo

# Register your models here.
@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    """ User information admin"""

    list_display = ('pk', 'user', 'phone_number', 'department',  'picture')
    list_display_links = ('pk', 'user',)
    list_editable = ('phone_number', 'picture', 'department')
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
    readonly_fields = ('created', 'modified',)


class UserinfoInline(admin.StackedInline):
    """Userinfo in-line admin for users."""

    model = Userinfo
    can_delete = False
    verbose_name_plural = 'Users info'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (UserinfoInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(Menu)
