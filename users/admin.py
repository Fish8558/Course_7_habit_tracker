from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'telegram_chat_id', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('email', 'telegram_chat_id',)
