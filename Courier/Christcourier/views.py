from django.shortcuts import render, HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User         
from Christcourier.models import New_User, P_Details


def index(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=Email,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('reci')
        else:
            return render(request,"user/index.html")
    return render(request,"user/index.html")
    

def service(request):
    return render(request,"user/service.html")

def about(request):  
    return render(request,"user/about.html")

def contact(request):
    return render(request,"user/contact.html")

def reci(request):
    return render(request,"user/reci.html")

def register(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Name = request.POST.get('Name')
        Phone_Number = request.POST.get('Phone_Number')
        reg_Number = request.POST.get('Reg_No')
        pass1 = request.POST.get('pass')

        my_user = User.objects.create_user(Email,Name,pass1)
        my_user.save()


        Regs=New_User(email=Email,
        name=Name,
        phone=Phone_Number,
        reg_no=reg_Number)
        Regs.save()
        return redirect('index')    
    return render(request,"user/reg.html")

def receive(request):
    
    if request.method=="POST":
        Id = request.POST.get('parcelId')
        email = request.POST.get('recEmail')
        Recname = request.POST.get('recName')
        Recphone = request.POST.get('recContact')  # Assuming recContact is the correct name
        Deldate = request.POST.get('delDate')
        Company = request.POST.get('company')
        
        add=P_Details(
            rec_id=Id,
            rec_email=email,
            rec_name=Recname,
            rec_phone=Recphone,
            reg_date=Deldate,
            rec_company=Company
        )
        add.save()
        # data = add.save()
        # if data:
    #         print("save")
    #     else:
    #         print("no") 
    # else:
    #     print("Not in Cond")           

    return render(request,"admin/receive.html")

def dashboard(request):
    return render(request,"user/dashboard.html")

def  staff(request):
    return render(request,"staff.html")

def staffreg(request):
    return render(request,"staffreg.html")

def adashboard(request):
    return render(request,"admin/adashboard,html")
