from django.urls import path, register_converter

from tablesReader import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('workers/<int:worker_id>/', views.workers, name='worker_id'),
    path('archive/<year4:year>/', views.archive, name='archive')
]