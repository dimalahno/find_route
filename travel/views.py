from django.shortcuts import render

def home(request):
    name = 'Dima'
    return render(request, 'home.html', {'name':name})