from django.db import models

# Create your models here.
class New_User(models.Model):
    email=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    reg_no=models.CharField(max_length=200)


    

  
