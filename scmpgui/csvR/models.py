# csvR/models.py
from django.db import models

class ExcelFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ExcelRow(models.Model):
    excel_file = models.ForeignKey(ExcelFile, on_delete=models.CASCADE)
    identification_no = models.CharField(max_length=255)
    sample_no = models.CharField(max_length=255)
    farm = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    lac_no = models.CharField(max_length=255)
    dim = models.CharField(max_length=255)
    avg_daily_my = models.CharField(max_length=255)
    test_day_my = models.CharField(max_length=255)
    fat = models.CharField(max_length=255) 
    snf = models.CharField(max_length=255)
    density = models.CharField(max_length=255)
    protein = models.CharField(max_length=255) 
    conductivity = models.CharField(max_length=255) 
    ph = models.CharField(max_length=255) 
    freezing_point = models.CharField(max_length=255)  
    salt = models.CharField(max_length=255)  
    lactose = models.CharField(max_length=255) 
    scc = models.CharField(max_length=255)  
    label = models.CharField(max_length=255)