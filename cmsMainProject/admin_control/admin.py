from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'Product_Name', 'Company_Name', 'display_product_image', 'Product_Price', 'Entered_By')
    list_filter = ('Product_Name','Company_Name')
    def display_product_image(self, obj):
        return format_html('<img src="{}" width="90" height="90" />', obj.Product_Image.url)
    
admin.site.register(Product,ProductAdmin)





class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'contact_number', 'location', 'entered_by')
admin.site.register(Doctor,DoctorAdmin) 




class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'time', 'entered_by')
    list_filter = ('doctor', 'date', 'entered_by')
    search_fields = ('doctor__name', 'entered_by__username')
admin.site.register(Appointment,AppointmentAdmin)


class dealadmin(admin.ModelAdmin):
    list_display=('doctor','product','quantity_ordered','entered_by')
admin.site.register(Deal,dealadmin)

class vistadmin(admin.ModelAdmin):
    list_display=('visit_date','location','is_successful')