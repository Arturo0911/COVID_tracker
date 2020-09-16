from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .api_functions import api
# Create your views here.
import json



def index_general(request):
    #api._create_object()
    return JsonResponse({'value': 'Reactjs'})

def general_page(request):

    return HttpResponse("Another page")
