from django import forms
from .models import *

#not useful
class ExcelFileUploadForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ['file']

#form for add and edit data
class DataForm(forms.ModelForm):
    class Meta:
        model = Batchdataset
        fields = ('id_num', 'sample_num', 'farm', 'breed', 'lactation_num', 'dim',
          'avg_daily_milk_yield', 'test_day_milk_yield', 'fat_percentage',
          'snf_percentage', 'milk_density', 'protein_percentage',
          'milk_conductivity', 'milk_ph', 'freezing_point', 'salt_percentage',
          'lactose_percentage', 'scc', 'label')


