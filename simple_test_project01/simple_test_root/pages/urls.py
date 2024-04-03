# simple_test_root/pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('kpop', views.about, name = 'about'),
    path('', views.index, name='index'),
]