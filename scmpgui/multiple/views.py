from django.shortcuts import get_object_or_404, redirect,render
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

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

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
            return redirect('index')
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

    return render(request, template, context)

