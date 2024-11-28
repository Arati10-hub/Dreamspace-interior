from django.urls import path
from . import views
from .views import ProductDetailView

urlpatterns=[
    path('',views.ProductListView.as_view(),name="products"),
    path('products/<int:pk>/',views.ProductDetailView.as_view(),name="product-detail"),
      path('create-product/',views.ProductCreateView.as_view(),name="create-product"),
    path('update-product/<int:pk>/',views.ProductUpdateView.as_view(),name="product-update"),
    path('delete-product/<int:pk>/',views.ProductDeleteView.as_view(),name="product-delete"),
    path('search',views.search,name="search"),
    path('<slug:slug>/',views.CategoryDetailView.as_view(),name="category-detail"),
   

     
]