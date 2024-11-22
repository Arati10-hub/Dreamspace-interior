from django.urls import path
from . import views 


urlpatterns=[
path('',views.display_cart,name="cart"),
path('add-to-cart/<int:productId>/',views.add_to_cart,name="add-to-cart"),
]