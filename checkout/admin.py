from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "delivery_cost",
        "order_total",
        "order_items",
        "grand_total",
    )

    fields = (
        "order_number",
        "date",
        "full_name",
        "email",
        "phone_number",
        "country",
        "postcode",
        "town_or_city",
        "street_address1",
        "street_address2",
        "delivery_cost",
        "order_total",
        "order_items",
        "grand_total",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "delivery_cost",
        "order_total",
        "order_items",
        "grand_total",
    )

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
