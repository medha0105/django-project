from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('customer_details/',views.customerDetails,name="customer_details"),
    path('about/', views.about, name="about"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
]