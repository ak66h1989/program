from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context = {'context': 'text'}
    return render(request, 'index.html', context)
