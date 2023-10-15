from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# admin.site.register(item)
@admin.register(Batchdataset)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('id_num', 'sample_num', 'farm', 'breed', 'lactation_num', 'dim',
          'avg_daily_milk_yield', 'test_day_milk_yield', 'fat_percentage',
          'snf_percentage', 'milk_density', 'protein_percentage',
          'milk_conductivity', 'milk_ph', 'freezing_point', 'salt_percentage',
          'lactose_percentage', 'label')

