from django.contrib import admin
from ecap.models import Contact
from ecap.models import Vendor,Product,Sales


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display=('vendor_name','vendor_phone_number')
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('prod_name','prod_id')
    
@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display=('bill_no','customer_name')