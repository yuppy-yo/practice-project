from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("Первая страница сайта.")

def workers(request, worker_id):
    return HttpResponse(f"<h1>Сотрудники</h1><p>id сотрудника: {worker_id}</p>")

def archive(request, year):
    if year > 2024:
        return redirect('home')
    return HttpResponse(f"<h1>АрХив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")