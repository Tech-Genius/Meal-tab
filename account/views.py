from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from . models import *
from . forms import *
from django.contrib.auth import login, authenticate, logout


# Create your views here.




def signup(request):
    form = Registration(request.POST)
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' ,Your account has been created succesfully.')
            return redirect('login')
        else:
            messages.info(request, 'Ooops! Cannot sign up, Kindly fix the errors')
    context = {'form' : form } 
    return render(request, 'signup.html', context)



def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('shop')
        else:
            messages.error(request,'Ooops! The details you entered do not match')
    context = {} 
    return render(request, 'login.html', context) 



def userlogout(request):
    logout(request)
    return redirect('login')


        
