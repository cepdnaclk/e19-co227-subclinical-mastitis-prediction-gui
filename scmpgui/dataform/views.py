from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Record
from django.urls import reverse
from .forms import DataForm
from external.model_helper import PredictPickle

# Create your views here.
def DataFormView(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        
        if form.is_valid():
            scm_status = PredictPickle(lactation_num=request.POST['lactation_num'],
                                        dim=request.POST['dim'],
                                        avg_daily_milk_yield=request.POST['avg_daily_milk_yield'],
                                        test_day_milk_yield=request.POST['test_day_milk_yield'],
                                        fat_percentage=request.POST['fat_percentage'],
                                        snf_percentage=request.POST['snf_percentage'],
                                        milk_density=request.POST['milk_density'],
                                        protein_percentage=request.POST['protein_percentage'],
                                        milk_conductivity=request.POST['milk_conductivity'],
                                        milk_ph=request.POST['milk_ph'],
                                        freezing_point=request.POST['freezing_point'],
                                        salt_percentage=request.POST['salt_percentage'],
                                        lactose_percentage=request.POST['lactose_percentage'])

            record = Record.objects.create(
                id_num=request.POST['id_num'],
                sample_num=request.POST['sample_num'],
                farm=request.POST['farm'],
                breed=request.POST['breed'],
                lactation_num=request.POST['lactation_num'],
                dim=request.POST['dim'],
                avg_daily_milk_yield=request.POST['avg_daily_milk_yield'],
                test_day_milk_yield=request.POST['test_day_milk_yield'],
                fat_percentage=request.POST['fat_percentage'],
                snf_percentage=request.POST['snf_percentage'],
                milk_density=request.POST['milk_density'],
                protein_percentage=request.POST['protein_percentage'],
                milk_conductivity=request.POST['milk_conductivity'],
                milk_ph=request.POST['milk_ph'],
                freezing_point=request.POST['freezing_point'],
                salt_percentage=request.POST['salt_percentage'],
                lactose_percentage=request.POST['lactose_percentage'],
                label=scm_status,
            )
            detail_url = reverse('results_from_record', args=[record.pk])
            # print(detail_url)
            return redirect(detail_url)
        
    else:
        form = DataForm()

    return render(request,"dataform/auto.html", {"form": form})


# def OldFormView(request):
#     if request.method == 'GET':
#         return render(request, "dataform/main.html", {})
#     elif request.method == 'POST':
#         record = Record.objects.create(
#             id_num=request.POST['id_num'],
#             sample_num=request.POST['sample_num'],
#             farm=request.POST['farm'],
#             breed=request.POST['breed'],
#             lactation_num=request.POST['lactation_num'],
#             dim=request.POST['dim'],
#             avg_daily_milk_yield=request.POST['avg_daily_milk_yield'],
#             test_day_milk_yield=request.POST['test_day_milk_yield'],
#             fat_percentage=request.POST['fat_percentage'],
#             snf_percentage=request.POST['snf_percentage'],
#             milk_density=request.POST['milk_density'],
#             protein_percentage=request.POST['protein_percentage'],
#             milk_conductivity=request.POST['milk_conductivity'],
#             milk_ph=request.POST['milk_ph'],
#             freezing_point=request.POST['freezing_point'],
#             salt_percentage=request.POST['salt_percentage'],
#             lactose_percentage=request.POST['lactose_percentage'],
#             scc=request.POST['scc'],
#             label=request.POST['label']
#         )
#         detail_url = reverse('results_from_record', args=[record.pk])
#         print(detail_url)
#         return redirect(detail_url)

# def form_submission(request):
#     if request.method == 'POST':
#         # Handle form submission and data processing here
#         # ...
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})