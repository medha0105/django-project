from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
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
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(user = user, )
            print(request.user.id)
            print(user.id)
            # messages.success(request, "Account created successully for " + username)
            return redirect('login')
    
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
    

def customerDetails(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)   #request.POST has all data submitted to customer_details url
        if form.is_valid():                 #is_valid is a method/function to check if form values are valid
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'cc/custom_details.html',context)


