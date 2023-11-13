from django.db import models

# Create your models here.

class ClientCodes(models.Model):
	OS_CHOICES = {
        ('windows', 'Windows'),
        ('linux', 'Linux'),
        ('macos', 'Mac OS'),
        ('debian', 'Debian'),
        ('openbsd', 'OpenBSD'),
    }

	OS = models.CharField(max_length = 30, choices = OS_CHOICES, default='windows')
	IAC = models.IntegerField(unique=True) #Internal accounting code
	DepCode = models.CharField(max_length = 8) #Department code