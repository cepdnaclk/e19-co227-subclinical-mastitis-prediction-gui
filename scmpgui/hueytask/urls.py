from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.addnum_view, name='add_num'),
    path('wait/',views.wait_test,name='wait_test'),
    path('wait/status/',views.check_task_status,name='check_task_status'),
    path('<str:task_id>/', views.get_task_result, name='get_task_result'),
]