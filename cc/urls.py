from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('customer_details/<str:pk>/',views.customerDetails,name="customer_details"),
    path('food_details/<str:pk1>/<int:pk2>/',views.foodDetails,name="food_details"),
    path('home/<str:pk>/',views.home,name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('profile/<str:pk>/', views.profilePage, name="profile_page"),
    path('daily_details/<str:pk>', views.dailyDetails,name="daily_details"),
    path('barchart/<str:pk>/', views.barchart, name="bar")
]