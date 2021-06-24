from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('customer_details/<str:pk>/',views.customerDetails,name="customer_details"),
    path('foodintake_details/<str:pk>/',views.foodDetails,name="food_details"),
    path('home/<str:pk>/',views.home,name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
]