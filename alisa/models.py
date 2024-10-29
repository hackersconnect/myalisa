from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import django.utils.timezone
from django_countries.fields import CountryField
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    phone=models.CharField(max_length=13,default=None,null=True, blank=True)
    id_number=models.IntegerField(default=0,blank=True,null=True)
    referee_email=models.EmailField(default=None,null=True)
    shop_name=models.CharField(max_length=50,null=True)
    gender=models.CharField(max_length=30,null=True,default=None)
    is_set=models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name
    
    class Meta:
        verbose_name='profile'
        verbose_name_plural='profiles'
        ordering=['user']

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250,default=None)
    description=models.TextField(max_length=300,default=None)
    category=models.ForeignKey('Category' ,on_delete=models.CASCADE,default=None)
    current_price=models.FloatField(default=0.00)
    previous_price=models.FloatField(default=0.00)
    rating=models.IntegerField(default=0)
    brand=models.CharField(max_length=250,default=None, null=True)
    slug = models.SlugField(default="", null=False)
    image=models.ImageField(upload_to='media/',default=None)
    is_sold=models.BooleanField(default=False)
    trending=models.BooleanField(default=False)
    featured=models.BooleanField(default=False)
    flash=models.BooleanField(default=False)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    added=models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='product'
        verbose_name_plural='products'
        ordering=['name']

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250,default=None)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
        ordering=['id']
    

class Cart(models.Model):
    id=models.AutoField(primary_key=True)
    product_link=models.ForeignKey('Product',on_delete=models.CASCADE,default=None)
    customer_link=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=0)
    added_date=models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(f'{self.quantity} * {self.product_link.name}')
    
    class Meta:
        verbose_name='cart'
        verbose_name_plural='carts'
        ordering=['id']
    

class Order(models.Model):
    id=models.AutoField(primary_key=True)
    product_link=models.ForeignKey('Product',on_delete=models.CASCADE,default=None)
    customer_link=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    payment_status=models.ForeignKey('Payment',on_delete=models.CASCADE,default=None)
    total_price= models.FloatField(default=0.00)
    status=models.BooleanField(default=False)
    order_time=models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name='order'
        verbose_name_plural='orders'
        ordering=['id']

class OrderItem(models.Model):
    id=models.AutoField(primary_key=True)
    order=models.ForeignKey('Order',on_delete=models.CASCADE,default=None)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,default=None)
    quantity=models.PositiveIntegerField(default=0)
    price=models.PositiveIntegerField(default=0)


    def __str__(self):
        return str(self.product)
    
    class Meta:
        verbose_name='orderitem'
        verbose_name_plural='orderitems'
        ordering=['id']
    







class Payment(models.Model):
    id=models.AutoField(primary_key=True)
    mode=models.CharField(max_length=50,default=None)
    reference_code=models.CharField(max_length=100,default=None, null=True)
    date=models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name='payment'
        verbose_name_plural='payments'
        ordering=['date']

class County(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default=None)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='county'
        verbose_name_plural='counties'
        ordering=['id']

class PickupStation(models.Model):
    id=models.AutoField(primary_key=True)
    town=models.ForeignKey('County', on_delete=models.CASCADE,default=None)
    station=models.CharField(max_length=100,default=None)


    def __str__(self):
        return self.station
    
    class Meta:
        verbose_name='pickupstation'
        verbose_name_plural='pickupstations'
        ordering=['id']

class CustomerAddress(models.Model):
    order=models.ForeignKey('Order',on_delete=models.CASCADE,default=None)
    county=models.CharField(max_length=250,default=None)
    station=models.CharField(max_length=250,default=None)
    phone=models.CharField(max_length=13,default=None)
    email=models.EmailField(null=True,default=None)


    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name='customer-address'
        verbose_name_plural='customer-addresses'
        ordering=['order']





class Foo(models.Model):
    country=CountryField()