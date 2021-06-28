from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import *
from .forms import *
from .caloriecalc import dummycalc
from .decorators import unauthenticated_user

def about(request):
    return render(request, 'cc/about.html')

@login_required(login_url = 'login')
def home(request, pk):
    #logic for daily calorie intake
    customer = Customer.objects.get(id=pk)
    foodItems = customer.food_set.all()
    breakfast = foodItems.filter(food_category="Breakfast")
    lunch = foodItems.filter(food_category="Lunch")
    snacks = foodItems.filter(food_category="Snacks")
    dinner = foodItems.filter(food_category="Dinner")

    calorieCount = dummycalc(pk)
    calorieConsumed = 0
    for item in foodItems:
        calorieConsumed += item.calories
    # print(calorieConsumed)
    caloriesLeft = calorieCount - calorieConsumed

    #logic for rendering pie chart
    data = []
    data.append(calorieConsumed)
    pieCarbs=0
    pieProteins=0
    pieFats=0
    for item in foodItems:
        pieCarbs += item.carbs
        pieProteins += item.proteins
        pieFats += item.fats  

    data.append(pieCarbs)
    data.append(pieProteins)
    data.append(pieFats)
    
    context = {'calorieCount':calorieCount,'breakfast':breakfast,'lunch':lunch,
    'snacks':snacks,'dinner':dinner,'calorieConsumed':calorieConsumed,'caloriesLeft':caloriesLeft,'data':data}
    return render(request,'cc/home.html',context)

@unauthenticated_user
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

@unauthenticated_user
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
    
@login_required(login_url = 'login')
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


@login_required(login_url = 'login')
def foodDetails(request,pk1,pk2=0):
    customer = Customer.objects.get(id=pk1)
    food_category = 'Breakfast'
    if pk2 == 1:
        food_category = 'Breakfast'
    elif pk2 == 2:
        food_category = 'Lunch'
    elif pk2 == 3:
        food_category = 'Snacks'
    elif pk2 == 4:
        food_category = 'Dinner'
        

    foodForm = FoodForm(initial={'customer':customer,'food_category':food_category})
    if request.method == "POST":
        foodForm = FoodForm(request.POST)
        if foodForm.is_valid():
            foodForm.save()
            return redirect('home', request.user.customer.id)
    context = {'foodForm':foodForm,'fields':['item','calories','carbs','proteins','fats']}
    return render(request,'cc/food_contents.html',context)


@login_required(login_url = 'login')
def profilePage(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {'customer':customer}
    return render(request, 'cc/profilePage.html', context)
