# csvR/forms.py
from django import forms
from .models import ExcelFile

class ExcelFileUploadForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ['file']
