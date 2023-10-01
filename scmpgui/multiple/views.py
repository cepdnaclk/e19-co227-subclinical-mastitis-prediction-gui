from django.shortcuts import  render
from .forms import ExcelFileUploadForm
import pandas as pd

#function for uplaod multiple data set
def upload_excel(request):
    if request.method == 'POST':
        form = ExcelFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.save()
            df = pd.read_excel(excel_file.file)
            return render(request, 'multiple/display_worksheet.html', {'df': df})
    else:
        form = ExcelFileUploadForm()
    return render(request, 'multiple/upload_excel.html', {'form': form})
