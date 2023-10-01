import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .models import HistoricalRecords
from .files import InitHistory
from dataform.models import Record

# Create your views here.
def InitData(request):
    InitHistory()
    return HttpResponse("Databse Loaded!")

def ViewHistory(request):

    #print(extracted_data)

    #return extracted_data

    # df = pd.read_excel('results\sampleInput.xlsx')
    df_1 = pd.read_excel('results\sampleOutput.xlsx')
    # #print(df)
    # inum = df.iloc[:, 0].tolist()
    # breed = df.iloc[:, 3].tolist()
    # lacnum = df.iloc[:, 4].tolist()
    # dim = df.iloc[:, 5].tolist()
    # yeild = df.iloc[:, 6].tolist()
    # fat = df.iloc[:, 8].tolist()
    # snf = df.iloc[:, 9].tolist()
    # density = df.iloc[:, 10].tolist()
    # ph = df.iloc[:, 13].tolist()

    # cow_id = df_1.iloc[2, 0].tolist()
    # cow_result = df_1.iloc[2, 1].tolist()

    all_results = df_1.iloc[:, 1].tolist()

    sample_num = HistoricalRecords.objects.values_list('sample_num')
    breed_new = HistoricalRecords.objects.values_list('breed')
    ph_new = HistoricalRecords.objects.values_list('milk_ph')

    #print(inum, lacnum)
    #return HttpResponse(df)
    # Create a context dictionary to pass the lists to the template

    number_list = list(range(1, 41))


    context = {
        """ 'inum': inum,
        'breed': breed,
        'lacnum': lacnum,
        'fat': fat,
        'snf': snf,
        'density': density,
        #'cow_id': cow_id,
        'cow_result': cow_result,
        'dim': dim,
        'yeild': yeild, """

        

        'num_lst': number_list,


        'ph' : ph_new,
        'all_results' : all_results,
        'breed_new' : breed_new,
        'sample_num' : sample_num,

    }

    # print(context['breed_new'])


    # Render the template with the context data
    return render(request,"history/main.html",context)

# def ViewHistory(request):

#     breed = HistoricalRecords.objects.values_list('breed')

#     context = {
#         'breed' : breed,
#     }

#     return render(request,"history/main.html",context)