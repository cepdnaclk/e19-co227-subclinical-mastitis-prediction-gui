from django.shortcuts import get_object_or_404, redirect, render
import pandas as pd
from .models import Batchdataset
from django.http import HttpResponse
from tablib import Dataset
from django.contrib import messages
from dataform.forms import DataForm
from .validators import *
from external.model_helper import PredictPickle

#function for import multiple dataets
def dataset_upload(request):
    if request.method == 'POST':
        dataset = Dataset()
        file = request.FILES.get('myfile')
        
        if not file:
            messages.error(request, 'Please select a file to upload.')
        elif not file.name.endswith(('.xlsx', '.xls')):
            messages.error(request, 'Invalid file type. Please upload an valid Excel file.')
        else:
            try:
                dataset.load(file.read(), format='xlsx')
                
                required_headers = ['Identification No', 'Sample No', 'Lac. No.', 'DIM( Days In Milk)', 'Avg(7 days). Daily MY( L )', 'Test day MY (L )', 'Fat (%)', 'SNF (%)', 'Density ( Kg/ m3', 'Protein (%)', 'Conductivity (mS/cm)', 'pH', 'Freezing point (⁰C)', 'Salt (%)', 'Lactose (%)']

                # Check for required headers
                if all(header in dataset.headers for header in required_headers):

                    field_mapping = {
                        'id_num': 'Identification No',
                        'sample_num': 'Sample No',
                        'farm': 'Farm',
                        'breed': 'Breed',
                        'lactation_num': 'Lac. No.',
                        'dim': 'DIM( Days In Milk)',
                        'avg_daily_milk_yield': 'Avg(7 days). Daily MY( L )',
                        'test_day_milk_yield': 'Test day MY (L )',
                        'fat_percentage': 'Fat (%)',
                        'snf_percentage': 'SNF (%)',
                        'milk_density': 'Density ( Kg/ m3',
                        'protein_percentage': 'Protein (%)',
                        'milk_conductivity': 'Conductivity (mS/cm)',
                        'milk_ph': 'pH',
                        'freezing_point': 'Freezing point (⁰C)',
                        'salt_percentage': 'Salt (%)',
                        'lactose_percentage': 'Lactose (%)',
                    }
                    
                    for data in dataset:
                        # Create a dictionary to store the field-value pairs
                        field_data = {}
                        
                        # Populate the dictionary using the mapping
                        for field, column in field_mapping.items():
                                index = dataset.headers.index(column)  # Find the index of the column in the dataset
                                field_data[field] = data[index]
                    
                        # Create a new Batchdataset object and save it
                        new_row = Batchdataset(**field_data)
                        new_row.save()

                    return redirect(display_dataset)
                else:
                    messages.error(request, "The dataset doesn't match the given template.")
                
            except Exception as e:
                error_type = type(e).__name__
                messages.error(request, f'Error importing data: {error_type}: {str(e)}')
    else:
        Batchdataset.objects.all().delete()
    
    return render(request, 'multiple/upload.html')


#function for display datasets
def display_dataset(request):
    items = Batchdataset.objects.all()

    #Validation
    overall_invalid = False

    for item in items:

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

    for item in items:
        scm_status = PredictPickle(lactation_num=item.lactation_num,
                                        dim=item.dim,
                                        avg_daily_milk_yield=item.avg_daily_milk_yield,
                                        test_day_milk_yield=item.test_day_milk_yield,
                                        fat_percentage=item.fat_percentage,
                                        snf_percentage=item.snf_percentage,
                                        milk_density=item.milk_density,
                                        protein_percentage=item.protein_percentage,
                                        milk_conductivity=item.milk_conductivity,
                                        milk_ph=item.milk_ph,
                                        freezing_point=item.freezing_point,
                                        salt_percentage=item.salt_percentage,
                                        lactose_percentage=item.lactose_percentage)
        item.label = scm_status

    context = {
        'items': items,
    }

    return render(request, 'multiple/result.html', context)
    
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

    return render(request,"multiple/form_extend.html", {"form": form})


#function for delet any dataset
def delete_data(request, pk):

    Batchdataset.objects.filter(pk=pk).delete()
    return redirect('multiple_display_dataset')

def delete_all_data(request):
    
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

def download_template_excel(request):
    # Define the required headers
    required_headers = ['Identification No', 'Sample No', 'Lac. No.', 'DIM( Days In Milk)', 'Avg(7 days). Daily MY( L )', 'Test day MY (L )', 'Fat (%)', 'SNF (%)', 'Density ( Kg/ m3', 'Protein (%)', 'Conductivity (mS/cm)', 'pH', 'Freezing point (⁰C)', 'Salt (%)', 'Lactose (%)']

    # Create a Pandas DataFrame with only the headers
    df = pd.DataFrame(columns=required_headers)

    # Create the HTTP response for the download
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="custom_excel.xlsx"'
    df.to_excel(response, index=False)

    return response