from django.db import models


class Car(models.Model):
    brand_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    car_number = models.CharField(max_length=100)
    total_seat = models.CharField(max_length=2)
    
    def __str__(self):
        return self.car_number
        

class CarStatus(models.Model):
    status = (
        ('AV', 'Available'),
        ('OT', 'On Travel'),
        ('IS', 'In Service'),
        ('AB', 'Booked'),
    )
    car_number = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_status = models.CharField(max_length=2, choices=status)    
    
    def __str__(self):
        return self.car_status
    
class Customer(models.Model):
    first_name      = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20)
    phone_number    = models.CharField(max_length=20)
    present_address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name 
    
    
class Driver(models.Model):
    first_name         = models.CharField(max_length=20)
    last_name          = models.CharField(max_length=20)
    phone_number       = models.CharField(max_length=20)
    driving_licence_no = models.CharField(max_length=200)
    present_address    = models.CharField(max_length=200)
    permanent_address  = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name 
    
    
class Location(models.Model):
    district_name         = models.CharField(max_length=20)
    distance_from_dhaka   = models.CharField(max_length=20)
    
    def __str__(self):
        return self.district_name
    
    
class RentCar(models.Model):
    customer      = models.ForeignKey(Customer, on_delete=models.CASCADE)
    journey_from  = models.ForeignKey(Location, on_delete=models.CASCADE)
    journey_to    = models.CharField(max_length=20)
    journey_date  = models.DateTimeField()
    car           = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver        = models.ForeignKey(Driver, on_delete=models.CASCADE)
    cost          = models.IntegerField()
    
    def __str__(self):
        return self.car.car_number