from django.contrib import admin

from .models import Car, CarStatus, Customer, Driver, Location, RentCar

admin.site.register(Car)
admin.site.register(CarStatus)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Location)
admin.site.register(RentCar)
