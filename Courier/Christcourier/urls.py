from django.urls import path
from Christcourier.views import index,service,about,reci,register,recipient,dashboard,profile,contact,sdashboard,receive,pstatus,admin_db,parcel,plot_graph,Return_,retdet

urlpatterns = [
    path  ('',index,name='index'),
    path  ('service',service,name='service'),
    path  ('about',about,name='about'), 
    path  ('contact',contact,name='contact'),
    path  ('reci',reci,name='reci'),
    path  ('reg',register,name='reg'),
    path  ('dashboard',dashboard,name='dashboard'),
    path  ('sdashboard',sdashboard,name='sdashboard'),
    path  ('receive',receive,name='receive'),
    path  ('pstatus',pstatus,name='pstatus'),
    path  ('admin_db',admin_db,name='admin_db'),
    path  ('parcel',parcel,name='parcel'),
    path  ('admindashboard',plot_graph,name='adminplot'),
    path  ('recipient',recipient,name='recipient'),
    path  ('Return',Return_,name='Return'),
    path  ('retdet',retdet,name='retdet'),
    path ('profile',profile,name='profile'),
]  

  
