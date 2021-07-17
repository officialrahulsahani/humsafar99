from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib import messages
from django import forms
from .models import *
from .forms import *



logstatus = None
b = None

def terms(request):
    return render(request, 'usermanager/terms.html')

def about(request):
    return render(request, 'usermanager/about.html')

def contact(request):
    return render(request, 'usermanager/contact.html')

def payment(request):
    return render(request, 'usermanager/payment.html')

def plans(request):
    return render(request, 'usermanager/plans.html')

def search(request):
    query = request.GET['query']
    alluser = User.objects.filter(name__icontains=query)
    return render(request, 'usermanager/search.html',{"alluser":alluser, "b":b})

def home(request):
    form = UserForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     return render(request, 'usermanager/.html', {"form": form})
    female = User.objects.all().filter(gender="Femal")[:6]
    male = User.objects.all().filter(gender="Male")[:2]
    return render(request, 'usermanager/home.html', {"form": form, 'female':female, 'male':male})

def login(request):
    global logstatus
    global b
    request.session['login_status'] = "0"
    form = LoginForm(request.POST)
    if (form.is_valid()):
        email = request.POST['email']
        password = request.POST['password']

        try:
            b = User.objects.get(email=email, password=password)
        except:
            b = False
            messages.error(request, "Your Email & Password is Incorrect")
        if (b):
            request.session['login_status'] = "1"
            logstatus = request.session['login_status']
            return render(request, "usermanager/myprofile.html", {"logstatus": logstatus, "b": b})
        else:
            return redirect('login')
    return render(request, 'usermanager/login.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Account is created ! You can login Now.")
            return redirect('login')
    form = UserForm()
    return render(request, 'usermanager/register.html', {"form":form})





def logout(request):
    request.session['login_status'] = None
    return render(request, 'usermanager/home.html')

def myprofile(request):
    if checklogin():
        return render(request, 'usermanager/myprofile.html', {"b":b})
    else:
        return render(request, 'usermanager/home.html')


def editprofile(request):
    if checklogin():
        p = b.pk
        u = get_object_or_404(User, pk=p)  # selct * from books where pk=8
        form = UserForm(request.POST or None, request.FILES or None, instance=u)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile has been updated ! Please Login again to see the Changes.")
            return render(request, 'usermanager/editprofile.html', {"b": b, "form": form})
        return render(request, 'usermanager/editprofile.html', {"b": b, "form": form})
    else:
        return render(request, 'usermanager/home.html')


def profile(request):
    if checklogin():
        social = User.objects.all()[:50]
        login_status = request.session['login_status']
        if (login_status == "1"):
            return render(request, 'usermanager/profile.html', {"b": b, "social": social})
        else:
            return render(request, 'usermanager/home.html')
    else:
        return render(request, 'usermanager/home.html')


def checklogin():
    global logstatus
    if (logstatus == "1"):
        return True
    else:
        return False







