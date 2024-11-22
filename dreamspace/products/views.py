from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView,ListView


# Create your views here.

def products(request):
    return render(request,"products.html")





def product_list(request):
    products = Product.objects.all()  # Get all products from the database
    return render(request, 'products.html', {'products': products})



class ProductDetailView(DetailView):
    model=Product
    template_name="products/productdetail.html"


class ProductListView(ListView):
    model=Product
    

def search(request):
    keyword=request.GET.get("keyword") 
    products=Product.customManager.all().filter(product_name__icontains=keyword)             
    return render(request,"products.html",{"products":products})
