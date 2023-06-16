from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('computer_entry/', views.computer_entry, name='computer_entry'),
    ]
1