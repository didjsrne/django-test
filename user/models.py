from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import RegexValidator


# Create your models here.

class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    phone = models.CharField(max_length = 16, default='')
    address = models.CharField(max_length=256, default='')