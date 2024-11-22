from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from products.models import Product
from .models import Cart,CartItem

# Create your views here.





def add_to_cart(request,productId):
    print("**********",productId,"************")
    print(request.user)
    currentUser=request.user
    cart,created=Cart.objects.get_or_create(user=currentUser)
    cartitem,created = CartItem.objects.get_or_create(cart = cart,products = Product.customManager.get(id = productId)) 
    quantity = int(request.GET.get("quantity")) #type cast in string 

    if created:
        cartitem.quantity = quantity
    else:
        cartitem.quantity += quantity 
    
    cartitem.save() #we are connected with the object
    return HttpResponseRedirect("/products")

def display_cart(request):
    currentUser = request.user
    cart = Cart.objects.get(user=currentUser)
    cartitems = cart.cartitem_set.all()
    total = 0
    for cartitem in cartitems:
        total += cartitem.quantity * cartitem.products.product_price
    return render(request,"cart.html",{"cartitems": cartitems,"total":total})


