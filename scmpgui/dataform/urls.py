from django.urls import path
from . import views

urlpatterns = [
    path("" , views.DataFormView, name='dataform'),
    path('submit/', views.form_submission, name='form_submission'),
]
