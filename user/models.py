from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import RegexValidator


# Create your models here.

class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    phoneRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators = [phoneRegex], max_length = 16, unique = True)
    address = models.CharField(max_length=256, blank=True, null=True)