# results/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.graph_view, name='results'),
]
