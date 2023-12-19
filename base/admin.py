from django.contrib import admin
from base.models import Currency


class EntityAdmin(admin.ModelAdmin):
    list_display = ("name", )


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("symbol", "name", "currency_type", "decimals")


admin.site.register(Currency, CurrencyAdmin)
