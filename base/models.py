from django.db import models
from base.constants import *


class Entity(models.Model):
    name = models.CharField(unique=True, max_length=LENGTH_ENTITY_NAME)

    class Meta:
        verbose_name_plural = "Entities"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# Create your models here.
class Currency(models.Model):
    TYPE_FIAT = "FIAT"
    TYPE_CRYPTO = "Crypto"

    CURRENCY_TYPES = [
        (TYPE_CRYPTO, TYPE_CRYPTO.upper()),
        (TYPE_FIAT, TYPE_FIAT.upper()),
    ]
    symbol = models.CharField(max_length=LENGTH_CURRENCY_SYMBOL, unique=True)
    name = models.CharField(max_length=LENGTH_CURRENCY_NAME)
    currency_type = models.CharField(max_length=16, choices=CURRENCY_TYPES)
    decimals = models.IntegerField(default=LENGTH_CURRENCY_DECIMALS_DEFAULT, null=False)

    class Meta:
        verbose_name_plural = "Currencies"

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    def __repr__(self):
        return f"{self.name} ({self.symbol})"

    def is_fiat(self):
        return self.currency_type == self.TYPE_FIAT

    def is_crypto(self):
        return self.currency_type == self.TYPE_CRYPTO
