from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_excel, name='upload_excel'),
    path("display/", views.index, name='display'),
    path("display_dataset/", views.display_dataset, name='display_dataset'),
]
