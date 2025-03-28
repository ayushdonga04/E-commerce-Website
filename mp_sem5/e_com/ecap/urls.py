from django.contrib import admin
from django.urls import path
from .import views
from .views import user_logout
from .views import add_vendor,add_product,add_sales


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('product',views.product,name="product"),
    path('about_us',views.about_us,name="about_us"),
    path('contact',views.contact,name="contact"),
    path('lg',views.lg,name="lg"),
    path('home',views.home,name="home"),
    path('vendor',views.vendor,name="vendor"),
    path('sell',views.sell,name="sell"), 
    path('collections/<int:product_id>/',views.purchase,name="purchase"), 
    path('logout/', user_logout, name='logout'),
    path('add-vendor/', add_vendor, name='add_vendor'),
    path('add-product/', add_product, name='add_product'),
    path('add-sales/', add_sales, name='add_sales'),
    path('purchase/<int:product_id>/', views.purchase, name='purchase'),
]
