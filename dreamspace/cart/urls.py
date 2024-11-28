from django.urls import path
from . import views 


urlpatterns=[
path('',views.display_cart,name="cart"),
path('add-to-cart/<int:productId>/',views.add_to_cart,name="add-to-cart"),
path('update-cart/<int:cartitemId>/',views.update_cart,name="update-cart"),
path('delete-cartitem/<int:cartitemId>/',views.delete_cartitem,name="delete-cartitem"),
path('checkout/',views.checkout,name="checkout"),
path('payment/<str:orderId>/',views.payment,name="payment"),
path('success/<str:orderId>/',views.paymentSuccess,name="success"),





]