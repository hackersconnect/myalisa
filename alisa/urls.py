#! /usr/bin/python3

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetView,PasswordResetCompleteView,PasswordResetConfirmView


urlpatterns=[
    path('',views.home_view, name='home'),
    path('super/local/dashboard/',views.admin_dashboard,name='admin-dashboard'),
    path('auth/user/login/', views.login_user, name='login_user'),
    path('view/cart/', views.view_cart, name='view_cart'),
    path('auth/user/add/', views.add_customer, name='add_customer'),
    path('auth/user/logout/', views.logout_user, name='logout_user'),
    path('user/<int:product_id>/add-cart/', views.add_cart, name='add_cart'),
    path('user/<int:item_id>/remove-cart/', views.minus_cart, name='remove_cart'),
    path('user/checkout-cart/', views.cart_checkout, name='checkout_cart'),
    path('cart/checkout-final/', views.checkOut, name='final_check'),
    path('product/<int:id>/detail-view/', views.detail_view, name='detail_view'),
    path('products/<str:category_name>/', views.category_view ,name='category_view'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
