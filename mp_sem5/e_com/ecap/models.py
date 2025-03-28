from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255)
    vendor_phone_number = models.CharField(max_length=20)
    business_name = models.CharField(max_length=255)
    date = models.DateField()
    product_name = models.CharField(max_length=255)
    product_quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    gst_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    gst_amount = models.DecimalField(max_digits=10, decimal_places=2)
    product_total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.vendor_name

class Product(models.Model):
    prod_name = models.CharField(max_length=255)
    prod_id = models.PositiveIntegerField()
    prod_adate = models.DateField()
    prod_qun = models.PositiveIntegerField()
    prod_price = models.DecimalField(max_digits=10, decimal_places=2)
    prod_gstp = models.DecimalField(max_digits=5, decimal_places=2)  
    prod_gstr = models.DecimalField(max_digits=10, decimal_places=2)  
    tprice = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return self.prod_name
    

class Sales(models.Model):
    bill_no = models.PositiveIntegerField(unique=True)
    customer_name = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)  # Adjust length as needed
    sale_date = models.DateField()
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gst_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Adjust as necessary
    gst_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale {self.bill_no} - {self.customer_name}"

