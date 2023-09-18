from django.db import models

class csvRModel(models.Model):
    column1 = models.CharField(max_length=255)
    column2 = models.CharField(max_length=255)
    # Add fields as needed for your CSV data
