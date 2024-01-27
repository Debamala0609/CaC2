from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"choto/index.html")
def service(request):
    return render(request,"choto/service.html")
def about(request):
    return render(request,"choto/about.html")
def contact(request):
    return render(request,"choto/contact.html")
