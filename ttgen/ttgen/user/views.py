from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.http import HttpResponse
import re


# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('psw1')
        pass2 = request.POST.get('psw2')


        
        if get_user_model().objects.filter(user_id=uid).exists():
            messages.error(request, 'User Id exists')
            return redirect('register')

        elif pass1 != pass2:
            messages.error(request, 'The passwords do not match')
            
            return redirect('register')
        elif get_user_model().objects.filter(email=email).exists():
            messages.error(request, 'This email is already registered')
            
            return redirect('register')

        else:
            User = get_user_model()
            new_user = User.objects.create_user(user_id=uid, name=name, email=email, password=pass1)

            return redirect('login')

        
        print('done')
        
    return render(request, 'user/register.html')



def usercheck(request):
    uid = request.POST.get('uid')
    if get_user_model().objects.filter(user_id=uid).exists():
        return HttpResponse('<div style="color:#ff1c3a; margin-top:6px;"> This User ID already exists.</div>')
    
    else:
        return HttpResponse('<div style="color:#04ff00; margin-top:6px;"></div>')



def login(request):

    if request.method =='POST':
        uid=request.POST.get('uid')
        password=request.POST.get('password')
        
        user= authenticate(request, user_id=uid, password=password)
        if user is not None:
            auth_login(request,user)
            print('redirect')
            return redirect('/')
        else:
            messages.error(request, 'Please enter valid userId and password')
        


    return render(request, 'user/login.html')