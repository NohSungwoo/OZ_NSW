from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin) :
    list_display = ('username', 'email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('username', 'phone_number')
    list_per_page = 10