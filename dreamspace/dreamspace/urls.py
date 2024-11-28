"""
URL configuration for dreamspace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
# adding urls.py from products application
from products import urls
from django.conf.urls.static import static
from . import settings
from cart import urls
from consulatant import urls
from django.urls import path







urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('gallary/',views.gallary),
    path('calculator/',views.calculator),
    path('products/',include('products.urls')),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('cart/',include('cart.urls')),
    path('consulatant/',include('consulatant.urls')),

]



urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)