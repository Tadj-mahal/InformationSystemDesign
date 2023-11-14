from django.forms import ModelForm
from django import forms
from .models import Client, Product


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ("name", "shopping_bag", "current_account",
                  "credit_limit", "current_doubt", "comment")


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ("name", "price", "stock_balance")
