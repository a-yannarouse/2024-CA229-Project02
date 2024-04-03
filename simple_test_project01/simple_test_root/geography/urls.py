from django.urls import path
from . import views

urlpatterns = [
    path('areas/', views.AreaList.as_view(), name='arealist'),
    path('attractions/', views.AttractionList.as_view(), name='attractionlist'),
    path("area/create", views.AreaCreate.as_view(), name="areacreate"),
    path("area/<pk>", views.AreaDetail.as_view(), name="areadetail"),
    path("area/update/<pk>", views.AreaUpdate.as_view(), name="areaupdate"),
    path("area/delete/<pk>", views.AreaDelete.as_view(), name="areadelete"),
    path('', views.geography_home, name='index'),
]