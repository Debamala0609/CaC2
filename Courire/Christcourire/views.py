from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"choto/index.html")
def service(request):
    return render(request,"choto/service.html")
def about(request):
    return render(request,"choto/about.html")
def contact(request):
<<<<<<< HEAD
    return render(request,"contact.html")
def reci(request):
    return render(request,"reci.html")
def reg(request):
    return render(request,"reg.html")
=======
    return render(request,"choto/contact.html")
>>>>>>> 6d4c31e17a299f530826aad45f4c154be064a28c
