from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader
# def index(request):
#     template = loader.get_template('myapp/index.html')
#     context = {
#     'test': 1,
#     }
#     return HttpResponse(template.render(context, request))


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    context = {'test': 1}
    return render(request, 'myapp/index.html', context)

# def test(request):
#     l = request.POST.getlist('choice')   #list object
#     for i in l:
#         print(i)
#     return render(request, 'myapp/index.html', {'l': l})

def test(request):
    l = request.POST.getlist('choice')   #list object
    for i in l:
        print(i)
    return render(request, 'myapp/testlist.html', {'l': l})