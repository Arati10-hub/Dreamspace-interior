from django.contrib import admin
from .models import Product,Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_price','product_description','product_brand']



class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','category_slug']


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)