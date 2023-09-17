# results/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.graph_view, name='results'),
]
