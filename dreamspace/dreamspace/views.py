from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import FileResponse, HttpResponse
import os
from django.conf import settings


def home(request):
    return render(request,"interior.html")

def gallary(request):
    return render(request,"interior_gallery.html")

def calculator(request):
    return render(request,"interior_c.html")



def register(request):
    if request.method=="GET":
        # form=UserCreationForm()
        form=CustomUserCreationForm()
        return render(request,"register.html",{"form":form})
    else:
        # form=UserCreationForm(request.POST)
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login")
        return render(request,"register.html",{"form":form})




def user_login(request):
    if request.method=="GET":
       return render(request,"login.html")
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print(request.user.first_name)
            return HttpResponseRedirect("/products")
        else:
            return render(request,"login.html",{"message":"User login failed"})
        


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")







def download_pdf(request):
    
    file_path = os.path.join(settings.BASE_DIR,'static','img', "guidline.pdf")
    
   
    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf', as_attachment=True, filename='guidline.pdf')
    except FileNotFoundError:
        return HttpResponse("File not found", status=404)


