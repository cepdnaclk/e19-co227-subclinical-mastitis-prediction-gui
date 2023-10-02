# results/views.py
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .models import ResultData
from dataform.models import Record

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

