# results/views.py
import csv
from django.shortcuts import render
from .models import ResultData

def graph_view(request):
    data = []  # List to store data from CSV file
    
    # Read data from CSV file and populate the data list
    with open('results/sampleInput.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row if present
        for row in reader:
            idNum, lacNum = row
            data.append({'Identification No': idNum, 'Lac. No.': lacNum})

    return render(request, 'results/graph.html', {'data': data})
