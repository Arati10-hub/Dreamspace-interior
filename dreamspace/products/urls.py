from django.urls import path
from . import views
from .views import ProductDetailView

urlpatterns=[
    path('',views.ProductListView.as_view(),name="products"),
    path('products/<int:pk>/',views.ProductDetailView.as_view(),name="product-detail"),
    path('search',views.search,name="search"),
    

     
]