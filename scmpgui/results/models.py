# results/models.py
from django.db import models

class ResultData(models.Model):
    idNum = models.IntegerField()
    lacNum = models.IntegerField()

