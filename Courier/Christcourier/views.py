from django.shortcuts import render
# from django.shortcuts import render , redirect
# from django.contrib.auth import authenticate , login , logout
# from django.contrib.auth.models import User
# Create your views here.
    
def login(request):
    return render(request,"index.html")

def index(request):
    return render(request,"user/index.html")

def service(request):
    return render(request,"user/service.html")

def about(request):
    return render(request,"user/about.html")

def contact(request):
    return render(request,"user/contact.html")

def reci(request):
    return render(request,"user/reci.html")

def reg(request):
    return render(request,"user/reg.html")

def dashboard(request):
    return render(request,"dashboard.html")
def  staff(request):
    return render(request,"staff.html")
def staffreg(request):
    return render(request,"staffreg.html")