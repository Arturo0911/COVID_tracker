from django.shortcuts import render
from django.http import HttpResponse
from .csv import index
# Create your views here.

def Index(request):

    #print(index.create_data())
    for x in index.create_data('Ecuador'):
        print(x)
    return render(request, 'prediction_model/index.html', {'covid':index.create_data('Ecuador')})


