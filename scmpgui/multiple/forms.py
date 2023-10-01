from django import forms
from .models import ExcelFile

#form for multiple input
class ExcelFileUploadForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ['file']
