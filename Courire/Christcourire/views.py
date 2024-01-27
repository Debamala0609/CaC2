from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def service(request):
    return render(request,"service.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def reci(request):
    return render(request,"reci.html")
def reg(request):
    return render(request,"reg.html")
