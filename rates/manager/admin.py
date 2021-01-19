from django.contrib import admin

from .models import Employee,Shipmentair,Shipmentfcl,Shipmentlcl,Shipmentroadeu,Shipmentroadus

# Register your models here.


from import_export.admin import ImportExportModelAdmin

admin.site.register(Employee)


@admin.register(Shipmentair,Shipmentfcl,Shipmentlcl,Shipmentroadeu,Shipmentroadus)

class ViewAdmin(ImportExportModelAdmin):
    pass
