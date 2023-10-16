from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
import pandas as pd
from .models import *
from django.http import HttpResponse
from .resources import *
from tablib import *
from django.contrib import messages
from dataform.forms import DataForm
from .validators import *

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

    #Validation
    overall_invalid = False

    for item in items:
        print(item.sample_num,item.avg_daily_milk_yield==None)

        validity = [
            StrictNumeric(item.id_num),
            StrictNumeric(item.sample_num),
            #TODO farm
            CowBreeds(item.breed),
            StrictNumeric(item.lactation_num),
            StrictNumeric(item.dim),
            #TODO Rest of the fields
        ]

        if any(i is False for i in validity):
            item.invalid = True
            overall_invalid = True if overall_invalid is False else overall_invalid
    
    if overall_invalid:
        bt_state = "disabled"
    else:
        bt_state = ""

    context = {
        'bt_state' : bt_state,
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
    print(items)

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

    
#function for edit any dataset
def edit_data(request, pk):

    # Assuming you have a primary key (pk) to identify the instance
    instance = get_object_or_404(Batchdataset, pk=pk)

    if request.method == 'POST':
        # If the form is submitted, process the data
        form = DataForm(request.POST)
        if form.is_valid():
            # Update the instance with the form data
            instance.id_num = form.cleaned_data['id_num']
            instance.sample_num = form.cleaned_data['sample_num']
            instance.farm = form.cleaned_data['farm']
            instance.breed = form.cleaned_data['breed']
            instance.lactation_num = form.cleaned_data['lactation_num']
            instance.dim = form.cleaned_data['dim']
            instance.avg_daily_milk_yield = form.cleaned_data['avg_daily_milk_yield']
            instance.test_day_milk_yield = form.cleaned_data['test_day_milk_yield']
            instance.fat_percentage = form.cleaned_data['fat_percentage']
            instance.snf_percentage = form.cleaned_data['snf_percentage']
            instance.milk_density = form.cleaned_data['milk_density']
            instance.protein_percentage = form.cleaned_data['protein_percentage']
            instance.milk_conductivity = form.cleaned_data['milk_conductivity']
            instance.milk_ph = form.cleaned_data['milk_ph']
            instance.freezing_point = form.cleaned_data['freezing_point']
            instance.salt_percentage = form.cleaned_data['salt_percentage']
            instance.lactose_percentage = form.cleaned_data['lactose_percentage']
        
            # Save the updated instance
            instance.save()
            # Redirect or do something else after successful update
            return redirect('multiple_display_dataset')
    else:
        # If it's a GET request, create the form with initial data
        initial_data = {
            'id_num': instance.id_num,
            'sample_num': instance.sample_num,
            'farm': instance.farm,
            'breed': instance.breed,
            'lactation_num': instance.lactation_num,
            'dim': instance.dim,
            'avg_daily_milk_yield': instance.avg_daily_milk_yield,
            'test_day_milk_yield': instance.test_day_milk_yield,
            'fat_percentage': instance.fat_percentage,
            'snf_percentage': instance.snf_percentage,
            'milk_density': instance.milk_density,
            'protein_percentage': instance.protein_percentage,
            'milk_conductivity': instance.milk_conductivity,
            'milk_ph': instance.milk_ph,
            'freezing_point': instance.freezing_point,
            'salt_percentage': instance.salt_percentage,
            'lactose_percentage': instance.lactose_percentage,
        }
        form = DataForm(initial=initial_data)

    return render(request,"dataform/auto.html", {"form": form})


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