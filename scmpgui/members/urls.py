from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='members_login'),
    path('register/', views.register_page, name='members_register'),
    path('logout/', views.logout_user, name='members_logout'),
] 