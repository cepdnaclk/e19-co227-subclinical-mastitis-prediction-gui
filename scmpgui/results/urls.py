# results/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("save/<int:pk>/", views.save_record, name="result_save_record"),
    path("<int:pk>/", views.result_from_record, name="results_from_record"),
    # path('', views.graph_view, name='results'),
]
