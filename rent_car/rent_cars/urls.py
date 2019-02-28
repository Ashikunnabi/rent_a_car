"""rent_car URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import * 

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    
    path('add_car', AddCarView.as_view(), name="add_car"),
    path('car/<car_id>', EditCarView.as_view(), name="edit_car"),
    path('car/<car_id>/delete', DeleteCarView.as_view(), name="delete_car"),
    
    path('add_customer', AddCustomerView.as_view(), name="add_customer"),
    path('customer/<customer_id>', EditCustomerView.as_view(), name="edit_customer"),
    path('customer/<customer_id>/delete', DeleteCustomerView.as_view(), name="delete_customer"),
    
    path('add_driver', AddDriverView.as_view(), name="add_driver"),
    path('driver/<driver_id>', EditDriverView.as_view(), name="edit_driver"),
    path('driver/<driver_id>/delete', DeleteDriverView.as_view(), name="delete_driver"),
    
    path('add_location', AddLocationView.as_view(), name="add_location"),
    path('location/<location_id>', EditLocationView.as_view(), name="edit_location"),
    path('location/<location_id>/delete', DeleteLocationView.as_view(), name="delete_location"),
    
    path('add_rent_car', AddRentCarView.as_view(), name="add_rent_car"),
    path('rent_car/<rent_car_id>', EditRentCarView.as_view(), name="edit_rent_car"),
    path('rent_car/<rent_car_id>/delete', DeleteRentCarView.as_view(), name="delete_rent_car"),
    
    path('add_car_status', AddCarStatusView.as_view(), name="add_car_status"),
    path('car_status/<car_status_id>', EditCarStatusView.as_view(), name="edit_car_status"),
    path('car_status/<car_status_id>/delete', DeleteCarStatusView.as_view(), name="delete_car_status"),
]
