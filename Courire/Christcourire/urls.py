from django.urls import path
from Christcourire import views 

urlpatterns = [
    path  ('',views.index,name='home'),
    path  ('service',views.service,name='Service'),
    path  ('about',views.about,name='About'), 
    path  ('contact',views.contact,name='Contact'),
]