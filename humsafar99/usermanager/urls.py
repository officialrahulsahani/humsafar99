
from django.contrib import admin
from django.urls import path
from usermanager import views
urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('myprofile/', views.myprofile, name="myprofile"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('profile/', views.profile, name="profile"),
    path('terms/', views.terms, name="terms"),
    path('about/', views.about, name="about"),
    path('plans/', views.plans, name="plans"),
    path('search/', views.search, name="search"),

]
