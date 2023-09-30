from django.contrib import admin
from .models import HistoricalRecords

# Register your models here.
class HistroyAdmin(admin.ModelAdmin):
    pass

admin.site.register(HistoricalRecords,HistroyAdmin)
