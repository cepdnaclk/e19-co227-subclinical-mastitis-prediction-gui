from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# admin.site.register(batchdataaset)
@admin.register(Batchdataset)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )

