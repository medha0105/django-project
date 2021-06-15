from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *

def about(request):
    return render(request, 'cc/about.html')

def home(request):
    return render(request,'cc/home.html')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # messages.success(request, "Account created successully for " + username)
            return redirect('customer_details')
    
    context={'form':form}
    return render(request, 'cc/register.html', context)

def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is incorrect")
    return render(request,'cc/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
    
def customerDetails(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)   #request.POST has all data submitted to customer_details url
        if form.is_valid():                 #is_valid is a method/function to check if form values are valid
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'cc/custom_details.html',context)


