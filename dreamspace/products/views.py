from django.shortcuts import render
from .models import Product,Category
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


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
    



@method_decorator(staff_member_required,name="dispatch")
class ProductCreateView(CreateView):
    model=Product
    fields="__all__"
    success_url="/products"

@method_decorator(staff_member_required,name="dispatch")
class ProductUpdateView(UpdateView):
    model=Product
    fields="__all__"
    success_url="/products"


@method_decorator(staff_member_required,name="dispatch")
class ProductDeleteView(DeleteView):
    model=Product
    success_url="/products"



def search(request):
    keyword=request.GET.get("keyword") 
    products=Product.customManager.all().filter(product_name__icontains=keyword)             
    return render(request,"products/product_list.html",{"object_list":products})

class CategoryDetailView(DetailView):
    model=Category
    template_name="category/category_detail.html"
    slug_field="category_slug"
    context_object_name="category_obj"      


    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs)
        context["categories"]=Category.objects.all()
        return context
    








