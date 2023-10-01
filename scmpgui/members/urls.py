from django.urls import path
from . import views

urlpatterns = [
    path('login_page/', views.login_page, name='login'),
    path('register_page/', views.register_page, name='register'),
    path('logout_user/', views.logout_user, name='logout'),
    path('', views.initial_page, name='initial'),
] 