from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    search_fields = ('email', 'username')
    list_filter = ('is_active',)
    ordering = ('-created_at',)
    list_display = (
        'email', 'username', 'created_at', 'is_active'
    )
    fieldsets = (
        (None, {'fields': ('email', 'username', 'description',)}),
        ('Разрешения', {'fields': ('is_staff', 'is_active', 'groups')}),
        ('Другое', {'fields': ('id', 'created_at', 'updated_at')})
    )
    readonly_fields = ('id', 'created_at', 'updated_at')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'description', 'is_active', 'is_staff')}
         ),
    )
