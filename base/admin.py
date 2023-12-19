from django.contrib import admin
from base.models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("symbol", "name", "currency_type", "decimals")


admin.site.register(Currency, CurrencyAdmin)
