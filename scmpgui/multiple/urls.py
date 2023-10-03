from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_excel, name='upload_excel'),
    path("dataset_upload/", views.dataset_upload, name='dataset_upload'),
    path("index/", views.index, name='index'),
    path("display_dataset/", views.display_dataset, name='display_dataset'),
    path("add_data/", views.add_data, name='add_data'),
    path("edit_data/<int:pk>/", views.edit_data, name='edit_data'),
    path("delete_data/<int:pk>/", views.delete_data, name='delete_data'),
]
