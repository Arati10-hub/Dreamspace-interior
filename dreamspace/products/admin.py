from django.contrib import admin
from .models import Product

# Register your models here.
# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_price','product_description','product_brand']

admin.site.register(Product,ProductAdmin)

