from django.contrib import admin

from .models import Item, Order, Tax, Discount

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "price",
    ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "discount",
        "tax",
    ]

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = [
        "stripe_id",
    ]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = [
        "stripe_id",
    ]
