#Read csv
from django.urls import path
from . import views

urlpatterns = [
    path('csvR/', views.csvR, name='csvR'),
]