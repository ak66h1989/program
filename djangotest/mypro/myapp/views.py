from django.shortcuts import render

from django.http import HttpResponse

from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
#     context = {'context': 'text'}
#     return render(request, 'index.html', context)
