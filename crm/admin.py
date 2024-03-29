from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import User
from crm.models import  *

class CustomerAdmin(admin.ModelAdmin):
    model = Customer

class LeadAdmin(admin.ModelAdmin):
    model = Lead


admin.site.register(Lead, LeadAdmin) 
admin.site.register(Customer, CustomerAdmin) 
admin.site.register(ShippingAddress, CustomerAdmin)
admin.site.register(BillingAddress, CustomerAdmin)
