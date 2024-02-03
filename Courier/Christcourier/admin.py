from django.contrib import admin
from .models import New_User,P_Details,New_staff
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display=('email','name','phone','reg_no')

admin.site.register(New_User,Admin)

class Recipient(admin.ModelAdmin):
    list_display=('rec_id','rec_email','rec_name','rec_phone','reg_date','rec_company')

admin.site.register(P_Details,Recipient)

class Staff(admin.ModelAdmin):
    list_display=('s_name','s_email')

admin.site.register(New_staff,Staff)  



