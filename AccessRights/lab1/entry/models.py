from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	POSITION_CHOICES = {
        ('secretary', 'Secretary'),
        ('associate director', 'Associate Director'),
        ('director', 'Director'),
    }

	position = models.CharField(max_length = 150, choices = POSITION_CHOICES, default='secretary')
	address = models.CharField(max_length = 50, default='')
	phone = models.CharField(max_length = 14, default='')

	def __str__(self):
		return self.username
# Create your models here.
