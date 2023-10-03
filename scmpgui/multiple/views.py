from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
import pandas as pd
from .models import *
from .forms import *
from django.http import HttpResponse
from .resources import *
from tablib import *


from django.contrib import messages

#function for import multiple dataets
def dataset_upload(request):
    if request.method == 'POST':
        Batchdataset_resource = BatchdatasetResource()
        dataset = Dataset()
        new_dataset = request.FILES.get('myfile')
        
        if not new_dataset:
            messages.error(request, 'Please select a file to upload.')
        elif not new_dataset.name.endswith(('.xlsx', '.xls')):
            messages.error(request, 'Invalid file type. Please upload an Excel file.')
        else:
            try:
                imported_data = dataset.load(new_dataset.read(), format='xlsx')
                for data in imported_data:
                    value = Batchdataset(
                        data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8],
                        data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16],
                        data[17], data[18], data[19]
                    )
                    value.save()
                messages.success(request, 'File uploaded successfully.')
            except Exception as e:
                messages.error(request, f'Error importing data: {str(e)}')
    
    return render(request, 'multiple/upload_excel.html')


#function for upload multiple datasets
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

#basic function
def index(request):
    return render(request, 'multiple/display.html')

#function for display datasets
def display_dataset(request):
    items = Batchdataset.objects.all()
    context = {
        'items': items,
        'header': 'Dataset',
    }
    return render(request, 'multiple/display.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_dataset')

    else:
        form = cls()
        return render(request, 'multiple/form.html', {'form' : form})


def add_data(request):
    return add_item(request, DataForm)

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_dataset')
    else:
        form = cls(instance=item)

        return render(request, 'multiple/edit.html', {'form': form})

def edit_data(request, pk):
    return edit_item(request, pk, Batchdataset, DataForm)

def delete_data(request, pk):

    template = 'multiple/display.html'
    Batchdataset.objects.filter(id=pk).delete()

    items = Batchdataset.objects.all()

    context = {
        'items': items,
    }

    return redirect('display_dataset')

    #return render(request, template, context)

