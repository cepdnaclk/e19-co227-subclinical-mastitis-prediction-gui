# results/views.py
from django.shortcuts import render,redirect
from django.http import HttpResponse
from dataform.models import Record
from history.models import HistoricalRecords
from django.contrib.auth.decorators import login_required

@login_required
def result_from_record(request,pk):
    record = Record.objects.get(pk=pk)

    context = {
        'cow_result': record.label,
        'user_sample' : record.sample_num,
        'user_inum' : record.id_num,
        'user_breed': record.breed,
        'user_lacnum' : record.lactation_num,
        'user_dim' : record.dim,
        'user_yeild': record.avg_daily_milk_yield,
        'user_fat' : record.fat_percentage,
        'user_snf' : record.snf_percentage,
        'user_density': record.milk_density,
        'user_protein' : record.protein_percentage,
        'user_conductivity' : record.milk_conductivity,
        'user_ph' : record.milk_ph,
        'user_freezing' : record.freezing_point,
        'user_salt' : record.salt_percentage,
        'user_lactose' : record.lactose_percentage,
        'user_scc' : record.scc,

        'pk' : pk, #after this line you have to add the result also
    }

    return render(request, 'tst.html', context)

@login_required
def save_record(request,pk):
    try:
        # Step 1: Get the Record object by primary key (pk)
        record = Record.objects.get(pk=pk)
        
        # Step 2: Extract data from the Record object
        data_to_transfer = {
            'id_num': record.id_num,
            'sample_num': record.sample_num,
            'farm': record.farm,
            'breed': record.breed,
            'lactation_num': record.lactation_num,
            'dim': record.dim,
            'avg_daily_milk_yield': record.avg_daily_milk_yield,
            'test_day_milk_yield': record.test_day_milk_yield,
            'fat_percentage': record.fat_percentage,
            'snf_percentage': record.snf_percentage,
            'milk_density': record.milk_density,
            'protein_percentage': record.protein_percentage,
            'milk_conductivity': record.milk_conductivity,
            'milk_ph': record.milk_ph,
            'freezing_point': record.freezing_point,
            'salt_percentage': record.salt_percentage,
            'lactose_percentage': record.lactose_percentage,
            'scc': record.scc,  # Include this line if scc is present in Record
            'label': "1" if record.label == "True" else "0",  # Include this line if label is present in Record
            'user': request.user,  # Add the currently logged-in user
        }
    
        # Step 3: Create a new HistoricalRecords object with the extracted data
        HistoricalRecords.objects.create(**data_to_transfer)

        return redirect("home")

    except Record.DoesNotExist:
        # Handle the case where the Record object with the given pk does not exist
        pass