from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('submit/', views.submit_form, name='nome_url'),
]