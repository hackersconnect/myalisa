from django.contrib import admin
from .models import Payment,PickupStation,Product,Profile,Cart,Category,County,Order,CustomerAddress
# Register your models here.

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(PickupStation)
admin.site.register(Payment)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(County)
admin.site.register(Order)
admin.site.register(CustomerAddress)
