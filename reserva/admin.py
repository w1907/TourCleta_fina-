from django.contrib import admin
from reserva.models import OrderItem, Order


@admin.register(OrderItem)
class orderItemAdmin(admin.ModelAdmin):
	list_display = ('product', 'is_ordered', 'date_added', 'date_ordered',)


@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
	list_display = ('ref_code', 'owner', 'is_ordered', 'date_ordered',)