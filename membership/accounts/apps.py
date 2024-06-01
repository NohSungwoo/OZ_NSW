# sttings.py의 INSTALLED_APPS에 app클래스를 등록하여 사용한다.
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

