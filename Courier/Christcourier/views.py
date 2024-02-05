from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from matplotlib import pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from Christcourier.models import New_User, P_Details,Return
from django.db.models import Count

def index(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        pass1 = request.POST.get('pass')
        
        # Check if password matches for a specific user
        user = authenticate(request, username=username, password=pass1)
        print(user)
        
        if user is not None:
            # Check user role and redirect accordingly
            if user.is_superuser:
                login(request, user)
                return redirect('admin_db')
            elif user.is_staff:
                login(request,user)
                return redirect('sdashboard')
            else:
                login(request, user)
                return redirect('dashboard')
        else:
            # Handle invalid credentials
            return render(request, "user/index.html", {'error_message': 'Invalid credentials'})

    return render(request, "user/index.html")

def service(request):
    return render(request,"user/service.html")

def about(request):  
    return render(request,"user/about.html")

def contact(request):
    return render(request,"user/contact.html")

def reci(request):
    return render(request,"user/dashboard.html")

def register(request):
    if request.method == 'POST':
        usertype = request.POST.get('choice')
        Email = request.POST.get('Email')
        Name = request.POST.get('Name')
        Phone_Number = request.POST.get('Phone_Number')
        reg_Number = request.POST.get('Reg_No')
        pass1 = request.POST.get('pass')

        if usertype == 'staff':
            my_user = User.objects.create_user(username=Email,email=Email,password=pass1,first_name=Name,is_staff=True)
            my_user.save()
        else:
            my_user1 = User.objects.create_user(username=Email,email=Email,password=pass1,first_name=Name)
            my_user1.save()

        Regs=New_User(email=Email,
        name=Name,
        phone=Phone_Number,
        reg_no=reg_Number)
        Regs.save()
        return redirect('index')    
    return render(request,"user/reg.html")

def receive(request):
    if request.method == 'POST':
        usertype = request.POST.get('choice')
        Email = request.POST.get('Email')
        Name = request.POST.get('Name')
        Phone_Number = request.POST.get('Phone_Number')
        reg_Number = request.POST.get('Reg_No')
        pass1 = request.POST.get('pass')

        if usertype == 'staff':
            my_user = User.objects.create_user(username=Email,email=Email,password=pass1,first_name=Name,is_staff=True)
            my_user.save()
        else:
            my_user1 = User.objects.create_user(username=Email,email=Email,password=pass1,first_name=Name)
            my_user1.save()

        Regs=New_User(email=Email,
        name=Name,
        phone=Phone_Number,
        reg_no=reg_Number)
        Regs.save()
        return redirect('index')    
    return render(request,'user/receive.html')
   
        # data = add.save()
        # if data:
    #         print("save")
    #     else:
    #         print("no") 
    # else:
    #     print("Not in Cond")           

    return render(request,"user/receive.html")

def dashboard(request):
    return render(request,"user/dashboard.html")

def sdashboard(request):
    return render(request,"staff/sdashboard.html")
def pstatus(request):
    return render(request,"staff/pstatus.html")

def admin_db(request):
    return render(request,"admin/admin_db.html")

def parcel(request):
   
    details=P_Details.objects.all()
    return render(request,"admin/parcel.html",{'parcel':details})



def recipient(request):
    det=New_User.objects.all()
    return render(request,"admin/recipient.html",{'recipient':det})

# def plot_graph(request):
#     # Retrieve data from the database
#     data = P_Details.objects.values('reg_date', 'rec_company')

#     # Extract data for plotting
#     dates = [entry['reg_date'] for entry in data]
#     companies = [entry['rec_company'] for entry in data]

#     # Create a plot
#     plt.figure(figsize=(10, 6))
#     plt.scatter(dates, companies)
#     plt.title('Registration Date vs Company')
#     plt.xlabel('Registration Date')
#     plt.ylabel('Company')
#     plt.xticks(rotation=45)

#     # Save the plot to a BytesIO object
#     from io import BytesIO
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
    
#     # Clear the plot for the next use
#     plt.clf()

#     # Convert the BytesIO object to base64 for embedding in HTML
#     import base64
#     plot_image = base64.b64encode(buffer.read()).decode('utf-8')

    # Pass the base64 image to the template
    # return render(request, 'admin/dash.html', {'plot_image': plot_image})

def Return_(request):
    
    if request.method=="POST":
        Id = request.POST.get('pId')
        Rotp = request.POST.get('rOtp')
        Rname = request.POST.get('rName')
        Rdate = request.POST.get('rDate')  # Assuming recContact is the correct name
        Ser = request.POST.get('company')
        print(Id,Rotp,Rname,Rdate)
        ad=Return(
            p_id=Id,
            p_otp=Rotp,
            p_name=Rname,
            p_date=Rdate,
            p_ser=Ser,
        )
        ad.save()
        return redirect('dashboard')


    return render(request,"user/Return.html")




def plot_graph(request):
    # Graph 1: Bar graph between Names and Company
    data1 = P_Details.objects.values('rec_company').annotate(count=Count('rec_name'))
    companies = [entry['rec_company'] for entry in data1]
    counts = [entry['count'] for entry in data1]

    plt.figure(figsize=(8, 4))
    plt.bar(companies, counts)
    plt.xlabel('Companies')
    plt.ylabel('Number of Names')
    plt.title('Graph between Names and Company')

    buffer1 = BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    plt.clf()
    image_base64_1 = base64.b64encode(buffer1.read()).decode('utf-8')

    # Graph 2: Scatter plot between Registration Dates and Company
    data2 = P_Details.objects.values('reg_date', 'rec_company')
    dates = [entry['reg_date'] for entry in data2]
    companies_2 = [entry['rec_company'] for entry in data2]

    plt.figure(figsize=(8, 4))
    plt.scatter(dates, companies_2)
    plt.title('Registration Date vs Company')
    plt.xlabel('Registration Date')
    plt.ylabel('Company')
    plt.xticks(rotation=45)

    buffer2 = BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    plt.clf()
    image_base64_2 = base64.b64encode(buffer2.read()).decode('utf-8')

    # Graph 3: Pie chart of Company counts
    data3 = P_Details.objects.values('rec_company').annotate(count=Count('rec_name'))

    companies_pie = [entry['rec_company'] for entry in data3]
    counts_pie = [entry['count'] for entry in data3]

    plt.figure(figsize=(8, 8))
    plt.pie(counts_pie, labels=companies_pie, autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart of Company Counts')

    buffer3 = BytesIO()
    plt.savefig(buffer3, format='png')
    buffer3.seek(0)
    plt.clf()
    image_base64_3 = base64.b64encode(buffer3.read()).decode('utf-8')

    return render(request, "admin/dash.html", {'image_base64_1': image_base64_1, 'image_base64_2': image_base64_2, 'image_base64_3': image_base64_3})
