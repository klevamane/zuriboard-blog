from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=50,
        unique=True,
        error_messages={"unique": "A user with this email already exists"},
    )

    REQUIRED_FIELDS = ["firstname", "lastname", "password", "email"]
    USERNAME_FIELD = "email"
