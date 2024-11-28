from django.contrib import admin

from .models import Order,OrderItem

# Register your models here.
admin.site.register(Order)

class OderItemAdmin(admin.ModelAdmin):
    list_display=["order","products","quantity"]
admin.site.register(OrderItem,OderItemAdmin)