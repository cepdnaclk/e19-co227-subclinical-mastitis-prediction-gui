from django.urls import path

from . import views

urlpatterns = [
    path("HomePageView/", views.HomePageView, name="home"),
]