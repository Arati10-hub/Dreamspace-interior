from django.db import models
from django.contrib.auth.models import User
from products.models import Product   
# Create your models here.

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
                                                    
    products=models.ManyToManyField(Product,through="CartItem")


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    products=models.ForeignKey(Product,on_delete=models.PROTECT)
    