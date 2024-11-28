from django.db import models
from autoslug import AutoSlugField

class ProductCustomManager(models.Manager):
     def get_queryset(self):
          return super().get_queryset()  #to get all object
     
     

class Category(models.Model):
     category_name=models.CharField(max_length=100,null=False)
     category_slug=AutoSlugField(populate_from="category_name",unique=True)

     def __str__(self):
         return self.category_name





# Create your models here.
class Product(models.Model):
     product_name=models.CharField(max_length=100,null=False)
     product_description=models.CharField(max_length=200,null=False)
     product_price=models.PositiveIntegerField(default=0)
     product_image=models.ImageField(upload_to="products/")  
     product_brand=models.CharField(max_length=100)


 # one to many relationship then we use foreign key
     category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)


     customManager=ProductCustomManager()

     def __str__(self):
          return self.product_name
     

  



