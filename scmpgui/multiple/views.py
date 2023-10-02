from django.shortcuts import  render
from .forms import ExcelFileUploadForm
import pandas as pd
from .models import *
from .forms import *

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

def index(request):
    return render(request, 'multiple/display.html')

def display_dataset(request):
    items = Batchdataset.objects.all()
    context = {
        'items': items,
        'header': 'Dataset',
    }
    return render(request, 'multiple/display.html', context)

