from django.urls import path
from . import views

urlpatterns = [
    path("dataset_upload/", views.dataset_upload, name='multiple_dataset_upload'),
    path("index/", views.index, name='index'),
    path("display_dataset/", views.display_dataset, name='multiple_display_dataset'),
    path("display_result/", views.display_result, name='multiple_display_result'),
    path("add_data/", views.add_data, name='multiple_add_data'),
    path("edit_data/<int:pk>/", views.edit_data, name='multiple_edit_data'),
    path("delete_data/<int:pk>/", views.delete_data, name='multiple_delete_data'),
    path('delete_all_data/', views.delete_all_data, name='multiple_delete_all_data'),
    path('export_dataset/', views.export_dataset, name='multiple_export_dataset'),

]
