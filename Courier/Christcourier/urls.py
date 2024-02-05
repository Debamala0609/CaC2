from django.urls import path
from Christcourier.views import index,service,about,reci,register,dashboard,stafflogin,staffreg,contact,sdashboard,receive,pstatus,admin_db

urlpatterns = [
    path  ('',index,name='index'),
    path  ('service',service,name='service'),
    path  ('about',about,name='about'), 
    path  ('contact',contact,name='contact'),
    path  ('reci',reci,name='reci'),
    path  ('reg',register,name='reg'),
    path  ('dashboard',dashboard,name='dashboard'),
    path  ('stafflogin',stafflogin,name='stafflogin'),
    path  ('staffreg',staffreg,name='staffreg'),
    path  ('sdashboard',sdashboard,name='sdashboard'),
    path  ('receive',receive,name='receive'),
    path  ('pstatus',pstatus,name='pstatus'),
    path ('admin_db',admin_db,name='admin_db'),
]  
