from django.shortcuts import render


def home(request):
    return render(request,'cc/home.html')
    


