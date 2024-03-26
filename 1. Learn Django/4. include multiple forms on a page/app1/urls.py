from django.urls import path, include
from app1 import views


app_name = 'app1'
urlpatterns = [
    path('', views.home, name='home'),
    
    
]