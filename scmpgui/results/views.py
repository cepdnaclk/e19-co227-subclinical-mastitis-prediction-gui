# results/views.py
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .models import ResultData
from dataform.models import Record

def graph_view(request):
    df = pd.read_excel('results\sampleInput.xlsx')
    df_1 = pd.read_excel('results\sampleOutput.xlsx')
    #print(df)
    inum = df.iloc[:, 0].tolist()
    lacnum = df.iloc[:, 4].tolist()
    fat = df.iloc[:, 8].tolist()
    snf = df.iloc[:, 9].tolist()
    density = df.iloc[:, 10].tolist()

    cow_id = df_1.iloc[2, 0].tolist()
    cow_result = df_1.iloc[2, 1].tolist()
    #print(inum, lacnum)
    #return HttpResponse(df)
    # Create a context dictionary to pass the lists to the template


    context = {
        'inum': inum,
        'lacnum': lacnum,
        'fat': fat,
        'snf': snf,
        'density': density,
        'cow_id': cow_id,
        'cow_result': cow_result
    }

    # Render the template with the context data
    return render(request, 'graph.html', context)

def result_from_record(request,pk):
    record = Record.objects.get(pk=pk)
    
    """ extracted_data = {
        'field1_value': record.sample_num,
        'field2_value': record.lactation_num,
    } """

    #print(extracted_data)

    #return extracted_data

    df = pd.read_excel('results\sampleInput.xlsx')
    df_1 = pd.read_excel('results\sampleOutput.xlsx')
    #print(df)
    inum = df.iloc[:, 0].tolist()
    lacnum = df.iloc[:, 4].tolist()
    fat = df.iloc[:, 8].tolist()
    snf = df.iloc[:, 9].tolist()
    density = df.iloc[:, 10].tolist()

    cow_id = df_1.iloc[2, 0].tolist()
    cow_result = df_1.iloc[2, 1].tolist()

    #print(inum, lacnum)
    #return HttpResponse(df)
    # Create a context dictionary to pass the lists to the template


    context = {
        'inum': inum,
        'lacnum': lacnum,
        'fat': fat,
        'snf': snf,
        'density': density,
        'cow_id': cow_id,
        'cow_result': cow_result,

        'user_inum' : record.sample_num,
        'user_lacnum' : record.lactation_num,
        'user_fat' : record.fat_percentage,
        'user_snf' : record.snf_percentage,
        'user_density' : record.milk_density
    }

    #print(context['user_lacnum'])

    # Render the template with the context data
    return render(request, 'graph.html', context)
    
# from django.http import HttpResponse
# from django.template import loader

# def graph_view(request):
#  template = loader.get_template('graph.html')
#  return HttpResponse(template.render())
