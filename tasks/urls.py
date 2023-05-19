from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:task_id>/', views.mark_task_complete, name='mark_task_complete'),
    path('incomplete/<int:task_id>/', views.mark_task_incomplete, name='mark_task_incomplete'),
    path('send_email/<int:task_id>/', views.send_email, name='send_email'),
    path('make_phone_call/<int:task_id>/', views.make_phone_call, name='make_phone_call'),
]