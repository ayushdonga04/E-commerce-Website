from django.shortcuts import render,redirect, get_object_or_404
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from .models import Vendor,Product,Sales


# Create your views here.


def index(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')   
        password1=request.POST.get('password')
        password2=request.POST.get('password1')
        
        if password1!=password2:
            messages.error(request, "enter same password")
        else:    
            my_user=User.objects.create_user(uname,email,password1)
            return redirect('lg')
    return render(request, 'index.html')



def about_us(request):
    return render(request, 'about_us.html')

def vendor(request):
    vendors = Vendor.objects.all()  # Fetch all vendor records
    return render(request, 'vendor.html', {'vendors': vendors})


def sell(request):
    sales = Sales.objects.all()  
    return render(request, 'sell.html', {'sales': sales})

def home(request):
    return render(request, 'home.html')

def lg(request):  
    if request.method=='POST':
        uname=request.POST.get('uname')
        ps=request.POST.get('password')
        user=authenticate(request,username=uname,password=ps)
        print(uname,ps)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message="inavlid username or password"
            messages.error(request, "❌ Invalid Username or Password!")
            
        
    return render(request, 'lg.html')
   
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent sucessfully")
            return redirect('contact')
    else:
        form = ContactForm()
          
    return render(request, 'contact.html')

def user_logout(request):
    logout(request)
    return redirect('index')

def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def purchase(request,product_id):
    product = get_object_or_404(Product, id=product_id)   
    return render(request, 'purchase.html',{'product': product})

def add_vendor(request):
    if request.method == 'POST':
        vendor = Vendor(
            vendor_name=request.POST['vname'],
            vendor_phone_number=request.POST['vphone'],
            business_name=request.POST['shop_name'],
            date=request.POST['date'],
            product_name=request.POST['pname'],
            product_quantity=request.POST['pquantity'],
            product_price=request.POST['price'],
            gst_percentage=request.POST['gstp'],
            gst_amount=request.POST['gstr'],
            product_total_price=request.POST['tprice'],
            total_amount=request.POST['tamount'],
        )
        vendor.save()
        return redirect('product')
    return render(request, 'product.html')  


def add_product(request):
    if request.method == 'POST':
        product = Product(
            prod_name=request.POST['prod_name'],
            prod_id=request.POST['prod_id'],
            prod_adate=request.POST['prod_adate'],
            prod_qun=request.POST['prod_qun'],
            prod_price=request.POST['prod_price'],
            prod_gstp=request.POST['prod_gstp'],
            prod_gstr=request.POST['prod_gstr'],
            tprice=request.POST['tprice'],
        )
        product.save()
        return redirect('product')  
    return render(request, 'product.html')  


def add_sales(request):
    if request.method == 'POST':
        sales = Sales(
            bill_no=request.POST['bilno'],
            customer_name=request.POST['cname'],
            customer_address=request.POST['cadd'],
            phone_number=request.POST['cphone'],
            sale_date=request.POST['sdate'],
            product_name=request.POST['pnam'],
            quantity=request.POST['pqy'],
            price=request.POST['pprc'],
            gst_percentage=request.POST['pgstp'],
            gst_amount=request.POST['pgstr'],
            total_amount=request.POST['tamt'],
        )
        sales.save()
        return redirect('product')  
    return render(request, 'product.html')


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Product

def purchase(request, product_id):
    product = Product.objects.get(id=product_id)
    total_price = product.prod_price

    message = f"""
    New Purchase Order!
    Customer Name: {request.user.username}
    Product Name: {product.prod_name}
    Price: ₹{total_price}
    """

    send_mail(
        'New Order Received',
        message,
        'ayushdonga04@gmail.com',  # Sender Email
        ['ayushdonga04@gmail.com'],  # Receiver Email
        fail_silently=False,
    )

    return render(request, 'purchase.html', {'product': product})





