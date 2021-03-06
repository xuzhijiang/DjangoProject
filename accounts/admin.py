from django.contrib import admin
from .models import BlogUser


class BlogUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'username', 'email', 'last_login', 'date_joined')
    list_display_links = ('id', 'username')
