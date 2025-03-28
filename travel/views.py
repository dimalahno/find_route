from django.shortcuts import render

def home(request):
    name = 'Проект поиска маршрутов'
    return render(request, 'home.html', {'name':name})