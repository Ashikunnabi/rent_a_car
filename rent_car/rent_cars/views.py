from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import *
from django.views.generic.edit import FormView

from .forms import AddCarForm, AddCustomerForm, AddCarStatusForm, AddDriverForm, AddLocationForm, AddRentCarForm 
from .models import Car, CarStatus, Customer, Driver, Location, RentCar

## ================================== Index Page ============================================
class IndexView(TemplateView):
    template_name = 'rent_cars/index.html'
    
    def cards(self):
        context = {
            'total_car'        : Car.objects.all().count,
            'on_travel'        : CarStatus.objects.filter(car_status='OT').count,
            'in_service'       : CarStatus.objects.filter(car_status='IS').count,
            'advance_booking'  : CarStatus.objects.filter(car_status='AB').count,
        }
        return context        
        
    def get(self,request, **kwargs):
        context = {
            'cars'          : Car.objects.all(),
            'available_cars': Car.objects.filter(carstatus__car_status='AV')
        }                
        context['cards'] = self.cards()
        return render(request, self.template_name, context)
  
 ## ================================== Car Information Page ============================================ 
class AddCarView(FormView):
    template_name = 'rent_cars/add_car.html'
    form_class    = AddCarForm         
        
    def get(self,request, **kwargs):
        context = {
            'cars': Car.objects.all(),
            'form': self.form_class
        }                        
        return render(request, self.template_name, context)        
        
    def post(self,request, **kwargs):
        model = AddCarForm(request.POST)
        model.save()
        context = {
            'cars': Car.objects.all(),
            'form': self.form_class
        }                        
        return render(request, self.template_name, context)
      
  
class EditCarView(TemplateView):
    template_name = 'rent_cars/edit_car.html'
        
    def get(self,request, car_id, **kwargs):
        context = {
            'car': Car.objects.get(pk=car_id),
        }                        
        return render(request, self.template_name, context) 
                
    def post(self,request, car_id, **kwargs):    
        car_update = Car.objects.get(id=car_id)
        car_update.brand_name=request.POST['brand_name']
        car_update.model_name=request.POST['model_name']
        car_update.car_number=request.POST['car_number']
        car_update.total_seat=request.POST['total_seat']        
        car_update.save()
        
        context = {
            'car': Car.objects.get(id=car_id),
        }                        
        return render(request, self.template_name, context)
     
  
class DeleteCarView(TemplateView):
    template_name = 'rent_cars/edit_car.html'
        
    def get(self,request, car_id, **kwargs):
        return redirect("/add_car")         
        
        
    def post(self,request, car_id, **kwargs):    
        car_delete = Car.objects.get(id=car_id)        
        car_delete.delete()  
        return redirect("/add_car")              
  
 ## ================================== Car Status Page ============================================ 
class AddCarStatusView(FormView):
    template_name = 'rent_cars/add_car_status.html'
    form_class    = AddCarStatusForm         
        
    def get(self,request, **kwargs):
        context = {
            'car_statuss': CarStatus.objects.all(),
            'form'       : self.form_class
        }                        
        return render(request, self.template_name, context)        
        
    def post(self,request, **kwargs):
        model = AddCarStatusForm(request.POST)
        model.save()
        context = {
            'car_statuss': CarStatus.objects.all(),
            'form'       : self.form_class
        }                        
        return render(request, self.template_name, context)
      
  
class EditCarStatusView(TemplateView):
    template_name = 'rent_cars/edit_car_status.html'
        
    def get(self,request, car_status_id, **kwargs):
        context = {
            'cars'      : Car.objects.all(),
            'car_status': CarStatus.objects.get(pk=car_status_id),
        }                        
        return render(request, self.template_name, context) 
                
    def post(self,request, car_status_id, **kwargs): 
        car = Car.objects.get(car_number=request.POST['car_number'])   
        
        car_status_update = CarStatus.objects.get(id=car_status_id)   
        car_status_update.car_number=car    
        car_status_update.car_status=request.POST['car_status']      
        car_status_update.save()
        
        context = {
            'cars'      : Car.objects.all(),
            'car_status': CarStatus.objects.get(id=car_status_id),
        }                        
        return render(request, self.template_name, context)
     
  
class DeleteCarStatusView(TemplateView):
    template_name = 'rent_cars/edit_car_status.html'
        
    def get(self,request, car_status, **kwargs):
        return redirect("/add_car_status")         
        
        
    def post(self,request, car_status_id, **kwargs):    
        car_status_delete = CarStatus.objects.get(id=car_status_id)        
        car_status_delete.delete()  
        return redirect("/add_car_status")      
  
## ================================== Customer Information Page ============================================ 
class AddCustomerView(FormView):
    template_name = 'rent_cars/add_customer.html'
    form_class    = AddCustomerForm         
        
    def get(self,request, **kwargs):
        context = {
            'customers': Customer.objects.all(),
            'form'     : self.form_class
        }                        
        return render(request, self.template_name, context)        
        
    def post(self,request, **kwargs):
        model = AddCustomerForm(request.POST)
        model.save()
        context = {
            'customers': Customer.objects.all(),
            'form'     : self.form_class
        }                        
        return render(request, self.template_name, context)
      
  
class EditCustomerView(TemplateView):
    template_name = 'rent_cars/edit_customer.html'
        
    def get(self,request, customer_id, **kwargs):
        context = {
            'customer': Customer.objects.get(pk=customer_id),
        }                        
        return render(request, self.template_name, context) 
                
    def post(self,request, customer_id, **kwargs):    
        customer_update = Customer.objects.get(id=customer_id)
        customer_update.first_name=request.POST['first_name']
        customer_update.last_name=request.POST['last_name']
        customer_update.phone_number=request.POST['phone_number']
        customer_update.present_address=request.POST['present_address']        
        customer_update.save()
        
        context = {
            'customer': Customer.objects.get(id=customer_id),
        }                        
        return render(request, self.template_name, context)
     
  
class DeleteCustomerView(TemplateView):
    template_name = 'rent_cars/edit_customer.html'
        
    def get(self,request, customer_id, **kwargs):
        return redirect("/add_car")         
        
        
    def post(self,request, customer_id, **kwargs):    
        customer_delete = Customer.objects.get(id=customer_id)        
        customer_delete.delete()  
        return redirect("/add_customer")        
  
## ================================== Driver Information Page ============================================  
class AddDriverView(FormView):
    template_name = 'rent_cars/add_driver.html'
    form_class    = AddDriverForm         
        
    def get(self,request, **kwargs):
        context = {
            'drivers': Driver.objects.all(),
            'form'   : self.form_class
        }                        
        return render(request, self.template_name, context)        
        
    def post(self,request, **kwargs):
        model = AddDriverForm(request.POST)
        model.save()
        context = {
            'drivers': Driver.objects.all(),
            'form'   : self.form_class
        }                        
        return render(request, self.template_name, context)
      
  
class EditDriverView(TemplateView):
    template_name = 'rent_cars/edit_driver.html'
        
    def get(self,request, driver_id, **kwargs):
        context = {
            'driver': Driver.objects.get(pk=driver_id),
        }                        
        return render(request, self.template_name, context) 
                
    def post(self,request, driver_id, **kwargs):    
        driver_update = Driver.objects.get(id=driver_id)
        driver_update.first_name=request.POST['first_name']
        driver_update.last_name=request.POST['last_name']
        driver_update.phone_number=request.POST['phone_number']
        driver_update.driving_licence_no=request.POST['driving_licence_no']        
        driver_update.present_address=request.POST['present_address']        
        driver_update.permanent_address=request.POST['permanent_address']        
        driver_update.save()
        
        context = {
            'driver': Driver.objects.get(id=driver_id),
        }                        
        return render(request, self.template_name, context)
     
  
class DeleteDriverView(TemplateView):
    template_name = 'rent_cars/edit_driver.html'
        
    def get(self,request, driver_id, **kwargs):
        return redirect("/add_driver")         
        
        
    def post(self,request, driver_id, **kwargs):    
        driver_delete = Driver.objects.get(id=driver_id)        
        driver_delete.delete()  
        return redirect("/add_driver")           
  
## ================================== Location Information Page ============================================ 
class AddLocationView(FormView):
    template_name = 'rent_cars/add_location.html'
    form_class    = AddLocationForm         
        
    def get(self,request, **kwargs):
        context = {
            'locations': Location.objects.all(),
            'form'     : self.form_class
        }                        
        return render(request, self.template_name, context)        
        
    def post(self,request, **kwargs):
        model = AddLocationForm(request.POST)
        model.save()
        context = {
            'locations': Location.objects.all(),
            'form'     : self.form_class
        }                        
        return render(request, self.template_name, context)
      
  
class EditLocationView(TemplateView):
    template_name = 'rent_cars/edit_location.html'
        
    def get(self,request, location_id, **kwargs):
        context = {
            'location': Location.objects.get(pk=location_id),
        }                        
        return render(request, self.template_name, context) 
                
    def post(self,request, location_id, **kwargs):    
        location_update = Location.objects.get(id=location_id)
        location_update.district_name=request.POST['district_name']
        location_update.distance_from_dhaka=request.POST['distance_from_dhaka']      
        location_update.save()
        
        context = {
            'location': Location.objects.get(id=location_id),
        }                        
        return render(request, self.template_name, context)
     
  
class DeleteLocationView(TemplateView):
    template_name = 'rent_cars/edit_location.html'
        
    def get(self,request, location, **kwargs):
        return redirect("/add_location")         
        
        
    def post(self,request, location_id, **kwargs):    
        location_delete = Location.objects.get(id=location_id)        
        location_delete.delete()  
        return redirect("/add_location")           
  
## ================================== Car Rent Page ============================================  
class AddRentCarView(FormView):
    template_name = 'rent_cars/add_rent_car.html'
    form_class    = AddRentCarForm         
        
    def get(self,request, **kwargs):
        context = {
            'rent_cars': RentCar.objects.all(),
            'form'     : self.form_class
        }                        
        return render(request, self.template_name, context)        
        
    def post(self,request, **kwargs):
        model = AddRentCarForm(request.POST)
        model.save()
        context = {
            'rent_cars': RentCar.objects.all(),
            'form'     : self.form_class
        }                        
        return render(request, self.template_name, context)
      
  
class EditRentCarView(TemplateView):
    template_name = 'rent_cars/edit_rent_car.html'
        
    def get(self,request, rent_car_id, **kwargs):
        context = {
            'customers': Customer.objects.all(),
            'cars'     : Car.objects.all(),
            'drivers'  : Driver.objects.all(),
            'locations': Location.objects.all(),
            'rent_car' : RentCar.objects.get(pk=rent_car_id),
        }                        
        return render(request, self.template_name, context) 
                
    def post(self,request, rent_car_id, **kwargs):    
        customer     = Customer.objects.get(first_name=request.POST['customer'] )
        journey_from = Location.objects.get(district_name=request.POST['journey_from'] )
        car          = Car.objects.get(car_number=request.POST['car'])
        driver       = Driver.objects.get(first_name=request.POST['driver'] )
        
        rent_car_update = RentCar.objects.get(id=rent_car_id)
        rent_car_update.customer=customer
        rent_car_update.journey_from=journey_from    
        rent_car_update.journey_to=request.POST['journey_to']      
        rent_car_update.journey_date=request.POST['journey_date']      
        rent_car_update.car=car   
        rent_car_update.driver=driver   
        rent_car_update.cost=request.POST['cost']      
        rent_car_update.save()
        
        context = {
            'customers': Customer.objects.all(),
            'cars'     : Car.objects.all(),
            'drivers'  : Driver.objects.all(),
            'locations': Location.objects.all(),
            'rent_car' : RentCar.objects.get(id=rent_car_id),
        }                        
        return render(request, self.template_name, context)
     
  
class DeleteRentCarView(TemplateView):
    template_name = 'rent_cars/edit_rent_car.html'
        
    def get(self,request, rent_car, **kwargs):
        return redirect("/add_rent_car")         
        
        
    def post(self,request, rent_car_id, **kwargs):    
        rent_car_delete = RentCar.objects.get(id=rent_car_id)        
        rent_car_delete.delete()  
        return redirect("/add_rent_car")    
    