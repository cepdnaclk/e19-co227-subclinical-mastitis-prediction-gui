# csvR/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_excel, name='upload_excel'),
    path('edit_row/<int:row_id>/', views.edit_row, name='edit_row'),
]
