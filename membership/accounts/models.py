from django.db import models
from common.models import CommonModel
class Account(CommonModel) :
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length = 15, blank = True, null = True)

