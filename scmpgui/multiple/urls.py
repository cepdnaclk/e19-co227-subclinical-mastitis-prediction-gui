from django.urls import path
from . import views

urlpatterns = [
    path("dataset_upload/", views.dataset_upload, name='multiple_dataset_upload'),
    path("index/", views.index, name='index'),
    path("display_dataset/", views.display_dataset, name='multiple_display_dataset'),
    path("add_data/", views.add_data, name='multiple_add_data'),
    path("edit_data/<int:pk>/", views.edit_data, name='multiple_edit_data'),
    path("delete_data/<int:pk>/", views.delete_data, name='multiple_delete_data'),
]
