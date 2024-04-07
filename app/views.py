from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from random import randint
import asyncio

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        request.session['username'] = username 
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

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


@login_required(login_url="login")
def index(request):
     rm = random_with_N_digits(8)
     if request.method=='POST':
            i1 = request.FILES['file']
            filename = i1
            x = Nameoffile(user_id = rm, user_name = request.session['username'],file_name = filename,image = i1)
            x.save()
            
            messages.success(request, 'Uploaded Successfuly')
            return redirect('index')
     return render(request, "file_upload.html")