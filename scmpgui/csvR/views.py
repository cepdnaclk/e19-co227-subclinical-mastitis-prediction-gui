import csv
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import csvRModel  # Import my model for storing CSV data

#function for html file
def csvR(request):
    return render(request,'csvR.html')

#function for imoprt and read csv file
def import_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            # Add error handling for invalid file types
            return render(request, 'csvR/import_csv.html', {'error_message': 'Invalid file type'})

        # Assuming you have a model to store CSV data
        # Replace 'YourModel' with your actual model class
        for row in csv.reader(csv_file.read().decode('utf-8').splitlines()):
            csvRModel.objects.create(column1=row[0], column2=row[1])  # Replace with your model fields

        return HttpResponseRedirect('success/')  # Redirect to a success page

    return render(request, 'csvR.html')
