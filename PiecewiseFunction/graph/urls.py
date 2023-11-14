from django.contrib import admin
from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.PointAdd.as_view(), name = 'add_point'),
    path('interval/', views.gistogram, name = 'interval'),
    path('reset/', views.cleardata, name = 'clr_data'),
]
