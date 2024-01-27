from django.urls import path
from Christcourire import views 

urlpatterns = [
    path  ('',views.index,name='index'),
    path  ('service',views.service,name='service'),
    path  ('about',views.about,name='about'), 
    path  ('contact',views.contact,name='contact'),
    path  ('reci',views.reci,name='reci'),
    path  ('reg',views.reg,name='reg'),
    path  ('dashboard',views.dashboard,name='dashboard'),
    path  ('staff',views.staff,name='staff'),
    path  ('staffreg',views.staffreg,name='staffreg'),
    



]
