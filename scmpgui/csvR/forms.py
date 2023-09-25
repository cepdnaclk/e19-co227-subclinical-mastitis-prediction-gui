# csvR/forms.py
from django import forms
from .models import ExcelFile
from .models import ExcelRow


class ExcelFileUploadForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ['file']

class ExcelRowForm(forms.ModelForm):
    class Meta:
        model = ExcelRow
        fields = ['identification_no', 'sample_no', 'farm', 'breed', 'lac_no', 'dim', 'avg_daily_my', 'test_day_my', 'fat', 'snf', 'density', 'protein', 'conductivity', 'ph', 'freezing_point', 'salt', 'lactose', 'scc', 'label']
