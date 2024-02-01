from django.db import models

# Create your models here.
class New_User(models.Model):
    email=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    reg_no=models.CharField(max_length=200)

# class P_Details(models.Model):
#     rec_email=models.CharField(max_length=200)
#     rec_name=models.CharField(max_length=200)
#     rec_phone=models.CharField(max_length=200)
#     rec_no=models.CharField(max_length=200)




    

  
