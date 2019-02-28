from django import forms
from .models import Car, Customer, Driver, Location, RentCar, CarStatus


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields= '__all__'
        
        widgets = {
            'brand_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter brand name',}),
            'model_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter model name',}),
            'car_number': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter car number',}),
            'total_seat': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter total seat in car',}),
        }
        
        help_texts = {
            # 'brand_name': "We'll never share your email with anyone else.",
        }
        
        error_messages = {
            'total_seat': {
                'max_length': "We'll never share your email with anyone else.",
            }
        }


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields= '__all__'
        
        widgets = {
            'first_name'     : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter first name',}),
            'last_name'      : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter last name',}),
            'phone_number'   : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter phone number',}),
            'present_address': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter present address',}),
        }
        
        help_texts = {
            # 'brand_name': "We'll never share your email with anyone else.",
        }
        
        error_messages = {
        """
            'total_seat': {
                'max_length': "We'll never share your email with anyone else.",
            }
        """
        }


class AddDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields= '__all__'
        
        widgets = {
            'first_name'        : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter first name',}),
            'last_name'         : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter last name',}),
            'phone_number'      : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter phone number',}),
            'driving_licence_no': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter driving licence number',}),
            'present_address'   : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter present address',}),
            'permanent_address' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter permanent address',}),
        }
        
        help_texts = {
            # 'brand_name': "We'll never share your email with anyone else.",
        }
        
        error_messages = {
        """
            'total_seat': {
                'max_length': "We'll never share your email with anyone else.",
            }
        """
        }


class AddLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields= '__all__'
        
        widgets = {
            'district_name'        : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter district name',}),
            'distance_from_dhaka'  : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter distance',}),
            
        }
        
        help_texts = {
            # 'brand_name': "We'll never share your email with anyone else.",
        }
        
        error_messages = {
        """
            'total_seat': {
                'max_length': "We'll never share your email with anyone else.",
            }
        """
        }


class AddRentCarForm(forms.ModelForm):
    class Meta:
        model = RentCar
        fields= '__all__'
        
        widgets = {
            'customer'      : forms.Select(attrs={'class': 'form-control'}),
            'journey_from'  : forms.Select(attrs={'class': 'form-control'}),
            'journey_to'    : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter journey to',}),
            'journey_date'  : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter journey at',}),
            'car'           : forms.Select(attrs={'class': 'form-control','placeholder': 'Enter car number',}),
            'driver'        : forms.Select(attrs={'class': 'form-control'}),
            'cost'          : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter journey cost',}),
            
        }
        
        help_texts = {
            # 'brand_name': "We'll never share your email with anyone else.",
        }
        
        error_messages = {
        """
            'total_seat': {
                'max_length': "We'll never share your email with anyone else.",
            }
        """
        }


class AddCarStatusForm(forms.ModelForm):    
    class Meta:
        model = CarStatus
        fields= '__all__'
        
        widgets = {
            'car_number'   : forms.Select(attrs={'class': 'form-control'}),
            'car_status'   : forms.Select(attrs={'class': 'form-control'}),
            
        }
        
        help_texts = {
            # 'brand_name': "We'll never share your email with anyone else.",
        }
        
        error_messages = {
        """
            'total_seat': {
                'max_length': "We'll never share your email with anyone else.",
            }
        """
        }

