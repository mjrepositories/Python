from django.contrib import admin
from .models import Airlane

# Register your models here.

from import_export.admin import ImportExportModelAdmin

@admin.register(Airlane)
class ViewAdmin(ImportExportModelAdmin):
    pass