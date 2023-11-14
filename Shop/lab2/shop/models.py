from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.


def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is negative. Input positive number.'),
            params={'value': value},
        )


def validate_positive_not_null(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s is <= 0. Input positive number.'),
            params={'value': value},
        )


class Client(models.Model):
    name = models.CharField(max_length=70, )
    shopping_bag = models.IntegerField(
        default='0', validators=[validate_positive])  # сумма покупок
    current_account = models.IntegerField(
        validators=[validate_positive])  # текущий счёт клииента
    credit_limit = models.IntegerField(validators=[validate_positive])
    current_doubt = models.IntegerField(
        default='0', validators=[validate_positive])  # текущий долг
    # loan_balance = models.IntegerField(validators=[validate_positive]) #остаток кредита

    comment = models.CharField(max_length=500, default='')


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(validators=[validate_positive_not_null])
    stock_balance = models.IntegerField(
        validators=[validate_positive_not_null])  # Остаток на складе
