from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.views.decorators.cache import cache_control
# Create your views here.
# @login_required(login_url='login')
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')


def registerPage(request):
        form=UserCreationForm()
        if request.method=="POST":
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                messages.error(request,"Password does not follow the rules")
        context={'form':form}
        return render(request, 'register.html', context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request,"Username or Password is incorrect")
    return render(request,'login.html')


@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('login')
