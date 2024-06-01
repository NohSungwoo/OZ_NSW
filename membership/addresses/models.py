from django.db import models
from common.models import CommonModel
class Address(CommonModel) :
    user = models.ForeignKey('users.User', on_delete = models.CASCADE, related_name = 'nsw')
    street = models.TextField(max_length = 255)
    city = models.TextField(max_length = 100)
    state = models.TextField(max_length = 100)
    postal_code = models.TextField(max_length = 20)
    country = models.TextField(max_length = 100)