from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('sincrono/', views.sincrono_view),
    path('assincrono/', views.assincrono_view),
    path('fetch-teste-txt/', views.fetch_teste_txt),
    path('submit/', views.submit_form, name='nome_url'),
]