from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import *
from .forms import *
from .caloriecalc import dummycalc

def about(request):
    return render(request, 'cc/about.html')

def home(request, pk):
    #logic for daily calorie intake
    calorieCount = dummycalc(pk)
    context = {'calorieCount':calorieCount}
    return render(request,'cc/home.html',context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
        
            login(request, user)
            # messages.success(request, "Account created successully for " + username)
            return redirect('customer_details', request.user.customer.id)
    
    context={'form':form}
    return render(request, 'cc/register.html', context)

def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home', request.user.customer.id)
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
            return redirect('home', request.user.customer.id)

    context = {'form':form}
    return render(request,'cc/custom_details.html',context)


def foodDetails(request,pk):
    customer = Customer.objects.get(id=pk)
    form2 = FoodForm(instance=customer)
    if request.method == "POST":
        form2 = FoodForm(request.POST, instance=customer)   #request.POST has all data submitted to customer_details url
        if form2.is_valid():                 #is_valid is a method/function to check if form values are valid
            form2.save()
            return redirect('home', request.user.customer.id)

    context = {'form2':form2}
    return render(request,'cc/foodform.html',context)


def pieChart(request):
    data = []
    queryset = Food.objects.all()
    
    for food in queryset:
        data.append(food.calories)
        data.append(food.carbs)
        data.append(food.proteins)
        data.append(food.fats)
    context = {'data':data}
    return render(request,'cc/chart.html',context)