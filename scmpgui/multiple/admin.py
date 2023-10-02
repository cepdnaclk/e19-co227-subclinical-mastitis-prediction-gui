from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(item)
@admin.register(Batchdataset)
class ViewAdmin(admin.ModelAdmin):
    pass
