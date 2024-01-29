from django.shortcuts import render

# Create your views here.
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
    return render(request,"reg.html")
def login(request):
    return render(request,"index.html")
def dashboard(request):
    return render(request,"dashboard.html")
def  staff(request):
    return render(request,"staff.html")
def staffreg(request):
    return render(request,"staffreg.html")