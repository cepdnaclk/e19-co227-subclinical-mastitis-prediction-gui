# results/views.py
import csv
import pandas as pd
from django.shortcuts import HttpResponse, render
from .models import ResultData

def graph_view(request):
    df = pd.read_excel('results\sampleInput.xlsx')
    #print(df)
    inum = df.iloc[:, 0].tolist()
    lacnum = df.iloc[:, 4].tolist()
    #print(inum, lacnum)
    #return HttpResponse(df)
    # Create a context dictionary to pass the lists to the template
    context = {
        'inum': inum,
        'lacnum': lacnum,
    }

    # Render the template with the context data
    return render(request, 'graph.html', context)
    
# from django.http import HttpResponse
# from django.template import loader

# def graph_view(request):
#  template = loader.get_template('graph.html')
#  return HttpResponse(template.render())
