# 웹 서버는 Python으로 되어 있지 않기 때문에
# Python 기반의 프레임 워크인 django와 소통해줄 중간 개체가 필요하다.
"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
