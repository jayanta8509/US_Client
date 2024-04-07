from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalate Username')
            return redirect('login')
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request,'Invalate Password')
            return redirect('login')
        else :
            login(request ,user)
            return redirect('index')
    return render(request, "Client_Login_Page.html")


def logout_page(request):
    logout(request)
    return redirect ('login')

@login_required(login_url="login")
def index(request):
    return render(request, "Client_File_Upload_Page.html")