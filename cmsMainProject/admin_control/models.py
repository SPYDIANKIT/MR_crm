from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime


# Create your models


class Product(models.Model):
    Product_Name=models.CharField(max_length=50)
    Company_Name=models.CharField(max_length=50)
    Product_Image=models.ImageField( upload_to="media", height_field=None, width_field=None, max_length=None)
    Product_Price=models.FloatField(default=0,validators=[MinValueValidator(0)])
    Entered_By=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.Product_Name






def validate_contact_number(value):
    if len(str(value)) < 10:
        raise ValidationError("Contact number must have at least 10 digits.")
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_number = models.IntegerField( validators=[validate_contact_number])
    location = models.CharField(max_length=100)
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name






def future_date_validator(date):
    if date < timezone.now().date():
        raise ValidationError("you can not schedule on past dates select todays or future date ")
def validate_time_range(value):
    if not (9 <= value.hour <= 21):
        raise ValidationError("Scheduled time must be between 9 AM and 9 PM.")
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # ForeignKey relationship with the Doctor model
    date = models.DateField(validators=[future_date_validator])  # Date field for appointment date
    time = models.TimeField(validators=[validate_time_range])  # Time field for appointment time
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey relationship with the User model

    def __str__(self):
        return f"{self.doctor} - {self.date} - {self.time}-{self.entered_by}"
    def clean(self):
        future_date_validator(self.date)









class Deal(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_ordered = models.IntegerField(validators=[MinValueValidator(0)])
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.doctor} - {self.product}-{self.entered_by}"
    

