from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Fisability

@admin.register(Fisability)
class FisabilityAdmin(ImportExportModelAdmin):
    list_display = ('officename', 'pincode', 'circlename', 'regionname', 'availability')
    search_fields = ('officename', 'pincode', 'district', 'statename')
    list_filter = ('regionname', 'statename', 'availability')
