from django.urls import path
from Christcourire import views 

urlpatterns = [
    path  ('',views.index,name='home'),
    path  ('Service',views.index,name='Service'),
    path  ('About',views.index,name='About'), 
    path  ('Contact',views.index,name='Contact'),
]