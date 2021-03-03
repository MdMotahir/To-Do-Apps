from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
# Create your models here.


class User(AbstractUser):
    email=models.EmailField(unique=True)
    
    REQUIRED_FIELDS=('email','first_name','last_name',)

    def __str__(self):
        return self.username
    