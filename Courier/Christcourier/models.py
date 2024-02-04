from django.db import models
# Create your models here.
Company = (
    ('amazon','amazon'),
    ('flipkart','flipkart'),
    ('myntra','myntra'),
    ('nykaa','nykaa'),
    ('meesho','meesho'),
    ('others','others'),
)

class New_User(models.Model):
    email=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    reg_no=models.CharField(max_length=200)

class P_Details(models.Model):
    rec_id = models.CharField(max_length=50)
    rec_email = models.CharField(max_length=200)
    rec_name = models.CharField(max_length=200)
    rec_phone = models.CharField(max_length=200)
    reg_date = models.DateField()
    rec_company = models.CharField(max_length=200, choices=Company)

class New_staff(models.Model):
    s_name=models.CharField(max_length=200)
    s_email=models.CharField(max_length=200)
    




    

  
