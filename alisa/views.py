#! /usr/bin/python3
from math import ceil
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Cart,Category,County,CustomerAddress,Payment,PickupStation,Product,Profile,Order
# Create your views here.

def category_view(request,category_name):
    category=Category.objects.get(name=category_name)

    products=Product.objects.filter(category=category)

    return render(request,"alisa.html", {'products':products, 'category':category})

def home_view(request):
    cart_number=Cart.objects.filter(customer_link=request.user).count()
    
    
    products=Product.objects.all()
    return render(request, 'home.html',{'products':products, 'num':cart_number,})

#Show product detailed view
def detail_view(request,id):
    category=Category.objects.all()
    product=Product.objects.get(id=id)

    return render(request, 'detail.html', {'product':product, 'category':category})

#adding users or customers to the database creating user accounts
def add_customer(request):
    #receiving user credentials from the forms
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        #comparing passwords entered before saving
        if password1==password2:
            new_user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password2)
            new_user.save()
            return redirect('login_user')
        elif password1 != password2:
            messages.error(request, f'Password Mismatch')
            return redirect('add_customer')
        else:
            messages.error(request, f'User already exisits')
            return redirect('add_user')
    return render(request, 'log.html')
        


        
#this view plays the role of user authentication
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, f'Invalid Username or Password')
            return redirect('login_user')
    return render(request,'log.html')
# This view logsput a user who was previously authenticated
@login_required(login_url='login_user')
def logout_user(request):
    logout(request)
    return redirect('home')

#This Functions displays the admin dashboard only allowed for super users
@login_required(login_url='login_user')
def admin_dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request,'admin.html')
    
    return render(request, '404.html')
#This Fucntions Returns all items on the cart from the DB
def view_cart(request):
    ourCode='alisa@1'
    
    cart_items=Cart.objects.filter(customer_link=request.user)
    
    total_price=sum(item.product_link.current_price * item.quantity for item in cart_items)
    shipping_total=total_price + 300

    if request.method=='POST':
        promo_code=request.POST['code']
        if promo_code==ourCode:
            shipping_total=shipping_total - (0.2 * shipping_total)
        else:
            messages.error(request, f'InvalidCode!!')
            return redirect('view_cart')
    return render(request, 'new-cart.html', {'cart_items':cart_items, 'total_price':total_price,'grand_total':shipping_total})

#Adding Items To Your Shopping Cart
@login_required(login_url='login_user')
def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)

    cart_item, created = Cart.objects.get_or_create(product_link=product,customer_link=request.user)
    cart_item.quantity +=1

    cart_item.save()

    return redirect('final_check')

#This view deletes items previously added to cart
def minus_cart(request, item_id):
    cart_item=Cart.objects.get(id=item_id)
    cart_item.delete()
    return redirect('final_check')

@login_required(login_url='login_user')
def cart_checkout(request):
    cart_items=Cart.objects.filter(customer_link=request.user)
    
    total_price=sum(item.product_link.current_price * item.quantity for item in cart_items)
    shipping_total=total_price + 300
    cart_number = Cart.objects.filter(customer_link=request.user).count()
    towns=County.objects.all()
    stations=PickupStation.objects.all()
    return render(request, 'checkout.html', {'towns':towns, 'stations':stations, 'num':cart_number,'cart_items':cart_items, 'total_price':total_price, 'shipping':shipping_total})

#Final cart checkout including payment mode
@login_required(login_url='login_user')
def checkOut(request):
    ourCode='alisa@1'
    
    cart_items=Cart.objects.filter(customer_link=request.user)
    
    total_price=sum(item.product_link.current_price * item.quantity for item in cart_items)
    shipping_total=total_price + 300

    if request.method=='POST':
        promo_code=request.POST['code']
        if promo_code==ourCode:
            shipping_total=shipping_total - (0.2 * shipping_total)
        else:
            messages.error(request, f'InvalidCode!!')
            return redirect('view_cart')
    return render(request, 'new-cart.html', {'cart_items':cart_items, 'total_price':total_price,'grand_total':shipping_total})




