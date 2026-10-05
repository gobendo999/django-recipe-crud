from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'files/index.html')
def home(request):
    info = [
        {'Name': 'Gobenod Debanth', 'age': 30},
        {'Name': 'Gobenod Debanth', 'age': 15},
        {'Name': 'Gobenod Debanth', 'age': 25},
        {'Name': 'Gobenod Debanth', 'age': 17}, 
        {'Name': 'Gobenod Debanth', 'age': 24},
    ]

    return render(request, 'files/index.html', {'info': info})
    