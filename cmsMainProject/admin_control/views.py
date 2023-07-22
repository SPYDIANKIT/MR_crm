from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import logout

from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages  
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.Entered_By = request.user
            product.save()
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
from django.shortcuts import render





@login_required
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.entered_by = request.user
            doctor.save()
            messages.success(request,'Doctor Details Saved Successfully. ')
            return redirect('add_doctor')  # Redirect to the doctor list page
    else:
        form = DoctorForm()
    return render(request, 'add_doctor.html', {'form': form})






@login_required
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)



@login_required
def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.entered_by = request.user
            appointment.save()
            return redirect('success')
    else:
        form = AppointmentForm()
    
    return render(request, 'schedule_appointment.html', {'form': form})


@login_required
def todays_schedule(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')
        schedule = Appointment.objects.filter(date=selected_date,entered_by=request.user)
    else:
        selected_date = datetime.today().date()
        schedule = Appointment.objects.filter(date=selected_date,entered_by=request.user)
    
    context = {
        'selected_date': selected_date,
        'schedule': schedule
    }
    return render(request, 'todays_schedule.html', context)


@login_required
def enter_deal_details(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.entered_by = request.user  # Set the logged-in user as the creator of the deal
            deal.save()
            return redirect('completed_deals')
    else:
        form = DealForm()
    
    return render(request, 'enter_deal_details.html', {'form': form})


@login_required
def completed_deals(request):
    completed_deals = Deal.objects.filter(entered_by=request.user)
    return render(request, 'completed_deals.html', {'completed_deals': completed_deals})

def logout_user(request):
    logout(request)
    return redirect('visit_done')  # Redirect to the desired page after log out (change as needed)



def appointments_count_page(request):
    selected_date = datetime.today().date()
    schedule = Appointment.objects.filter(date=selected_date,entered_by=request.user)
    appointments_count = schedule.count()   
    print("Appointments Count:", appointments_count) 
    context = {
        'appointments_count': appointments_count,
    }
    return render(request, 'dashboard.html', context)

def get_appointments_count(request):
    current_date = datetime.today().date()
    appointments_count = Appointment.objects.filter(date=current_date, entered_by=request.user).count()
    
    return JsonResponse({'appointments_count': appointments_count})