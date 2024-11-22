from django.db import models

class ProductCustomManager(models.Manager):
     def get_queryset(self):
          return super().get_queryset()  #to get all object
     




# Create your models here.
class Product(models.Model):
     product_name=models.CharField(max_length=100,null=False)
     product_description=models.TextField(default="product description")
     product_price=models.PositiveIntegerField(default=0)
     product_image=models.ImageField(upload_to="products/")  
     product_brand=models.CharField(max_length=100)


     def __str__(self):
          return self.product_name
     

     customManager=ProductCustomManager()