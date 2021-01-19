from django.contrib import admin
from .models import home_bill,energy_bill,tv_bill,internet_bill,gas_bill
# Register your models here.


admin.site.register([gas_bill,tv_bill,internet_bill,energy_bill,home_bill])