from django.urls import path
from . import views

urlpatterns = [
    path("init/", views.InitData, name='history_init'),
    path("",views.ViewHistory,name='history_main')
]