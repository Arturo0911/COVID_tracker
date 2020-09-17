from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .api_functions import api
# Create your views here.
import json



def index_general(request):
    # print(api._create_object())
    # return JsonResponse({'data': values})
    # values = [{'value': 'Reactjs'}]
    return JsonResponse({'data': api._create_object()})

def general_page(request):

    return HttpResponse("Another page")
