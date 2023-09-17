# results/views.py
import csv
import pandas as pd
from django.shortcuts import HttpResponse, render
from .models import ResultData

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
    
# from django.http import HttpResponse
# from django.template import loader

# def graph_view(request):
#  template = loader.get_template('graph.html')
#  return HttpResponse(template.render())
