from django.contrib import admin
from .models import New_User
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display=('email','name','phone','reg_no')

admin.site.register(New_User,Admin)