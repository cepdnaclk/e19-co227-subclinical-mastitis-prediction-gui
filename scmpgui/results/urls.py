# results/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.result_from_record, name="result_record"),
    path('', views.graph_view, name='results'),
]
