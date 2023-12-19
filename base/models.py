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


class Account(models.Model):
    TYPE_ASSET = "Asset"
    TYPE_LIABILITIES = "Liabilities"
    TYPE_EQUITY = "Equity"
    TYPE_REVENUE = "Revenue"
    TYPE_EXPENSES = "Expenses"
    TYPE_RECEIVABLE = "Receivable"
    TYPE_PAYABLE = "Payable"

    ACCOUNT_TYPES = [
        (TYPE_ASSET, TYPE_ASSET.upper()),
        (TYPE_LIABILITIES, TYPE_LIABILITIES.upper()),
        (TYPE_EQUITY, TYPE_EQUITY.upper()),
        (TYPE_REVENUE, TYPE_REVENUE.upper()),
        (TYPE_RECEIVABLE, TYPE_RECEIVABLE.upper()),
        (TYPE_PAYABLE, TYPE_PAYABLE.upper()),
        (TYPE_EXPENSES, TYPE_EXPENSES.upper()),
    ]
    name = models.CharField(max_length=LENGTH_ACCOUNT_NAME, unique=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=32, choices=ACCOUNT_TYPES)

    @property
    def currency_symbol(self):
        return self.currency.symbol

    def __str__(self):
        return f"{self.name} ({self.currency_symbol} - {self.entity.name})"

    def __repr__(self):
        return f"{self.name} ({self.currency_symbol} - {self.entity.name})"
