from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
import pandas as pd
from .models import *
from .forms import *
from django.http import HttpResponse
from .resources import *
from tablib import *
from django.contrib import messages
from tabulate import tabulate


#function for import multiple dataets
def dataset_upload(request):
    if request.method == 'POST':
        Batchdataset_resource = BatchdatasetResource()
        dataset = Dataset()
        new_dataset = request.FILES.get('myfile')
        
        if not new_dataset:
            messages.error(request, 'Please select a file to upload.')
        elif not new_dataset.name.endswith(('.xlsx', '.xls')):
            messages.error(request, 'Invalid file type. Please upload an valid Excel file.')
        else:
            try:
                imported_data = dataset.load(new_dataset.read(), format='xlsx')
                for data in imported_data:
                    value = Batchdataset(
                        data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8],
                        data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16]
                    )
                    value.save()
                messages.success(request, 'Excel File uploaded successfully.')
            except Exception as e:
                messages.error(request, f'Error importing data: {str(e)}')
    
    return render(request, 'multiple/upload.html')


#basic function
def index(request):
    return render(request, 'multiple/display.html')


#function for display datasets
def display_dataset(request):
    items = Batchdataset.objects.all()
    context = {
        'items': items,
        'header': 'Dataset',#this is viewed in the page
    }
    return render(request, 'multiple/display.html', context)


#function for display results
def display_result(request):
    items = Batchdataset.objects.all()
    context = {
        'items': items,
    }
    model_fields = [field.name for field in Batchdataset._meta.fields]
    data = [[getattr(item, field) for field in model_fields] for item in items]
    headers = model_fields
    table = tabulate(data, headers, tablefmt="fancy_grid")
    print(table)

    return render(request, 'multiple/result.html', context)


#main functon for add any item
def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('multiple_display_dataset')

    else:
        form = cls()
        return render(request, 'multiple/form.html', {'form' : form})

#function for add any dataset
def add_data(request):
    return add_item(request, DataForm)


#main function for edit any item
def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('multiple_display_dataset')
    else:
        form = cls(instance=item)

        return render(request, 'multiple/edit.html', {'form': form})
    
#function for edit any dataset
def edit_data(request, pk):
    return edit_item(request, pk, Batchdataset, DataForm)


#function for delet any dataset
def delete_data(request, pk):

    template = 'multiple/display.html'
    Batchdataset.objects.filter(pk=pk).delete()

    items = Batchdataset.objects.all()

    context = {
        'items': items,
    }

    return redirect('multiple_display_dataset')

    #return render(request, template, context)

def delete_all_data(request):
    template = 'multiple/display.html'
    
    Batchdataset.objects.all().delete()
    return redirect('multiple_dataset_upload') 


def export_dataset(request):
    items = Batchdataset.objects.all()

    data = items.values('id_num', 'sample_num', 'label')
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="result_data.xlsx"'
    df.to_excel(response, index=False)

    return response