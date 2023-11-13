from django.forms import ModelForm
from django import forms
from .models import ClientCodes

class ClientCodesForm(ModelForm):
	class Meta:
		model = ClientCodes
		fields = ('IAC', 'OS',)