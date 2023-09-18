from django.shortcuts import render ,redirect
from .forms import ExcelFileUploadForm
import pandas as pd

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.save()
            # Assuming pandas library is installed
            df = pd.read_excel(excel_file.file)
            return render(request, 'display_worksheet.html', {'df': df})
    else:
        form = ExcelFileUploadForm()
    return render(request, 'upload_excel.html', {'form': form})
