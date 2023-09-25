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
    lac_no = models.CharField(max_length=255)  # For "Lac. No."
    dim = models.CharField(max_length=255)  # For "DIM( Days In Milk)"
    avg_daily_my = models.CharField(max_length=255)  # For "Avg(7 days). Daily MY( L )"
    test_day_my = models.CharField(max_length=255)  # For "Test day MY (L )"
    fat = models.CharField(max_length=255)  # For "Fat (%)"
    snf = models.CharField(max_length=255)  # For "SNF (%)"
    density = models.CharField(max_length=255)  # For "Density ( Kg/ m3"
    protein = models.CharField(max_length=255)  # For "Protein (%)"
    conductivity = models.CharField(max_length=255)  # For "Conductivity (mS/cm)"
    ph = models.CharField(max_length=255)  # For "pH"
    freezing_point = models.CharField(max_length=255)  # For "Freezing point (⁰C)"
    salt = models.CharField(max_length=255)  # For "Salt (%)"
    lactose = models.CharField(max_length=255)  # For "Lactose (%)"
    scc = models.CharField(max_length=255)  # For "SCC (103cells/ml)"
    label = models.CharField(max_length=255)