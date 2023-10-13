from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('login/', views.login_page, name='members_login'),
    path('register/', views.register_page, name='members_register'),
    path('logout/', views.logout_user, name='members_logout'),
    path('', RedirectView.as_view(url='login/',permanent=True))
] 