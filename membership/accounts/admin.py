# 관리자가 데이터베이스 모델을 관리하는 데 사용되는 파일이다.
from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin) :
    list_display = ('username', 'email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('username', 'phone_number')
    list_per_page = 10