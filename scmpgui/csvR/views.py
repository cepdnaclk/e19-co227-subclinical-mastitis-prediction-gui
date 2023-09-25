# csvR/views.py
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ExcelFileUploadForm, ExcelRowForm
from .models import ExcelFile, ExcelRow
import pandas as pd

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.save()
            df = pd.read_excel(excel_file.file)
            return render(request, 'csvR/display_worksheet.html', {'df': df})
    else:
        form = ExcelFileUploadForm()
    return render(request, 'csvR/upload_excel.html', {'form': form})

def edit_row(request, row_id):
    # Get the row object based on the row_id (replace ExcelRow with your actual model)
    row = get_object_or_404(ExcelRow, id=row_id)

    if request.method == 'POST':
        form = ExcelRowForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            return render(request, 'csvR/display_worksheet.html')
    else:
        form = ExcelRowForm(instance=row)

    return render(request, 'csvR/edit_row.html', {'form': form, 'row': row})