from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('username', 'email', 'is_staff')


admin.site.register(User, AccountAdmin)