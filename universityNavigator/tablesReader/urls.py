from django.urls import path, register_converter

from tablesReader import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index),
    path('workers/<int:worker_id>/', views.workers),
    path('archive/<year4:year>/', views.archive)
]