from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('create_user/', views.create_and_delete_user, name='create_user'),
    path('successful_user_creation', views.successful_user_creation, name='successful_user_creation'),
    path('user_in_database/', views.user_in_database, name='user_in_database'),
    path('list_users/', views.list_users, name='list_users'),
    path('create_task/', views.create_task, name='create_task'),
    path('successful_task_creation', views.successful_task_creation, name='successful_task_creation'),
    path('list_tasks/<int:user_id>/', views.list_tasks, name='list_tasks'),
    path('user_successfully_deleted', views.user_successfully_deleted, name='user_successfully_deleted'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]