from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 현재 프로젝트의 위치
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# django 웹서버 인증이 필요한 부분에서 사용되는 키
SECRET_KEY = 'django-insecure-4+g5d4yg%&f&0%y9jxmh^x_ya$0a7$ud2#mj!q7bu_#!stwx80'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 접속할 Host(domain)을 등록해줘야 한다.
ALLOWED_HOSTS = []


# Application definition
# 생성한 app들을 명시해 주어야 사용 가능하다.

DJANGO_SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_USER_APPS = [    
    'accounts.apps.AccountsConfig',
    'users.apps.UsersConfig',
    'addresses.apps.AddressesConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt'
    ]

INSTALLED_APPS = DJANGO_SYSTEM_APPS + CUSTOM_USER_APPS

# client 가 request 요청을하면 urldispatcher가 view에서 response를 반환한다.
# 해당 작업에 연관된 전처리를 해준다. 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 기준이 되는 url 파일의 경로를 의미한다.
ROOT_URLCONF = 'config.urls'

# Django에서 제공하는 Template의 기능들을 정의한다.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Web Server Gateway Interface
# 웹 서버에 동적 요청이 발생하면 WSGI 서버를 호출하고, WSGI는 파이썬 프로그램을 호출한다.
WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
# 비밀번호 복잡도
# createsuperuser 명령어를 실행할 때 비밀번호 선언 규칙
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME' : timedelta(minutes = 60),
    'REFRESH_TOKEN_LIFETIME' : timedelta(days = 14),
    'SIGNING_KEY' : 'SECRET',
    'ALGORITHM' : 'HS256',
    'AUTH_HEADER_TYPES' : ('Bearer',),
}