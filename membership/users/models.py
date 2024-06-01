from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser) :
    is_business = models.BooleanField(default = False)
    grade = models.CharField(max_length = 10, default = 'C')
    phone_number = models.CharField(max_length = 20)