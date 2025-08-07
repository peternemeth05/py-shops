from django.contrib import admin
from .models import Product, Offer

class ProductAdmin(admin.ModelAdmin): # admin is model imported from line 1, this module has a class named ModelAdmin, which has functionality for editing models in the admin
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

# Register your models here.
admin.site.register(Product, ProductAdmin) 
# using admin object imported in line 1
# this object has attribute site (which is also an object) which has method register


admin.site.register(Offer, OfferAdmin)