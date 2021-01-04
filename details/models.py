from django.db import models

# Create your models here.
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractBaseUser):
	name=models.CharField(max_length=100)
	email = models.EmailField(db_index=True, unique=True)

	dateofbirth = models.DateField( null=True)

	mobile_no = PhoneNumberField(max_length=13,blank=True,null=True)
	USERNAME_FIELD = 'email'
	def __str__(self):
		"""
		Returns a string representation of this `User`.
		This string is used when a `User` is printed in the console.
		"""
		return self.name




