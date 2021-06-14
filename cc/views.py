from django.shortcuts import render,redirect
from .models import *
from .forms import CustomerForm


def home(request):
    return render(request,'cc/home.html')

    
def customerDetails(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)   #request.POST has all data submitted to customer_details url
        if form.is_valid():                 #is_valid is a method/function to check if form values are valid
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'cc/custom_details.html',context)


