from django.contrib import admin

# Register your models here.

from .models import Instruction,Report,Business,Period,Status,Person,ReportingPeriod

from import_export.admin import ImportExportModelAdmin

@admin.register(Instruction,Report,Business,Period,Status,Person,ReportingPeriod)

class ViewAdmin(ImportExportModelAdmin):
    pass