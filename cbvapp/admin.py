from django.contrib import admin
from cbvapp.models import Company,Products,RentBooking 

# Register your models here.
admin.site.register(Company)
admin.site.register(Products)

@admin.register(RentBooking)
class RentBike(admin.ModelAdmin):
    list_display=['customer_name','customer_mobile','customer_ID','customer_driving_licence_id','Bike_name','bike_number']