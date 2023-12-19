from django.contrib import admin
from base.models import Account, Currency, Entity


class EntityAdmin(admin.ModelAdmin):
    list_display = ("name", )


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("symbol", "name", "currency_type", "decimals")


class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "get_entity_name", "get_currency_symbol",
                    "account_type")
    list_filter = ("entity", "currency", "account_type")

    def get_entity_name(self, obj):
        return obj.entity.name

    def get_currency_symbol(self, obj):
        return obj.currency_symbol

    get_entity_name.short_description = "Entity"
    get_currency_symbol.short_description = "Currency"


admin.site.register(Account, AccountAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Entity, EntityAdmin)
