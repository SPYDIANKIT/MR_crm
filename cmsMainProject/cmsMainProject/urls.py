"""
URL configuration for cmsMainProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from accounts.views import login_view, success_view,dashboard_view
from admin_control.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', login_view, name='login'),
    path('admin/', admin.site.urls,name="admin"),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('success/', success_view, name='success'),
    path('dashboard/',dashboard_view, name='dashboard'),
    path('add_product/', add_product, name='add_product'),
    path('add_doctor/', add_doctor, name='add_doctor'),
    path('product_list/', product_list, name='product_list'),
    path('schedule_appointment/', schedule_appointment, name='schedule_appointment'),
    path('todays_schedule/', todays_schedule, name='todays_schedule'),
    path('enter-deal-details/',enter_deal_details, name='enter_deal_details'),
    path('completed-deals/', completed_deals, name='completed_deals'),
    path('logout/', logout_user, name='logout'),
    path('appointments_count/', appointments_count_page, name='appointments_count_page'),
    path('get_appointments_count/', get_appointments_count, name='get_appointments_count'),
    # Other URL patterns...
   
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)