from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def DataFormView(request):
    if request.method == 'GET':
        return render(request, "dataform/main.html", {})
    elif request.method == 'POST':
        record = request.POST
        for key, value in request.POST.items():
            print(f"{key}: {value}")
        return HttpResponse("The form was submitted successfully.")

def form_submission(request):
    if request.method == 'POST':
        # Handle form submission and data processing here
        # ...
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})