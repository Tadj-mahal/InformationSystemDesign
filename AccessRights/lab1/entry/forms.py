from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username", "password1", "password2", "first_name", 
			"last_name", "position", "address", "phone")

class UserUpdateForm(ModelForm):
	class Meta:
		model = User
		fields = ("first_name", 
			"last_name", "position", "address", "phone")
	